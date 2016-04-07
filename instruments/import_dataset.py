import string
from common.models import *
import instruments.models
from instruments import import_dataset_helper


# Given a datasets's name (ex Marchman), dataset (ex Norming), language (ex English), instrument (ex WS), splitcol bool.
# Uses import_dataset_helper to retrieve the data from that dataset's data file, using its field and value mappings.
# Creates Child and Administration objects for the entries in the resulting data.
def import_dataset(dataset_name, dataset_dataset, dataset_file, instrument_language, instrument_form, splitcol, norming, date_format):

        var_safe = lambda s: ''.join([c for c in '_'.join(s.split()) if c in string.letters + '_'])
        instrument_string = var_safe(instrument_language) + '_' + var_safe(instrument_form)
        try:
            instrument_model = getattr(instruments.models, instrument_string)
        except AttributeError:
            raise IOError("instrument %s has no model defined" % instrument_string)

        import_helper = import_dataset_helper.ImportHelper(dataset_file, date_format, norming, splitcol)
        import_helper.import_data()

        instruments_map = Instrument.objects.get(language=instrument_language, form=instrument_form)

        children = {}

        for i, child_data in import_helper.children.iteritems():

            # initialize the Child here
            child = Child.objects.create(study_id=child_data['study_id'])
            child.date_of_birth = child_data['date_of_birth']
            child.sex = child_data['sex']
            child.birth_order = child_data['birth_order']
            if child_data['momed'] is not None:
                child.momed = MomEd.objects.get(level__iexact = child_data['momed'])
            child.study_momed = child_data['study_momed']
            child.ethnicity = child_data['ethnicity']

            children[i] = child
            child.save()

        for i, administration_data in import_helper.administrations.iteritems():

            instrument_obj = instrument_model.objects.create()
            administration = Administration.objects.create(child=children[i],
                                                           norming=administration_data['norming'],
                                                           date_of_test=administration_data['date_of_test'],
                                                           instrument=instruments_map,
                                                           data_id=instrument_obj.pk,
                                                           age=administration_data['age'],
                                                           data_age=administration_data['data_age'])

            administration.source = Source.objects.get(name=dataset_name,
                                                      dataset=dataset_dataset,
                                                      instrument_language=instrument_language,
                                                      instrument_form=instrument_form)

            instrument_model.objects.filter(pk=instrument_obj.pk).update(**administration_data['item_data'])

            administration.save()
