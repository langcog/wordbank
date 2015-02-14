from common.models import *
import instruments.models
from import_dataset_helper import ImportHelper


def import_dataset(dataset_name, dataset_dataset, dataset_file, instrument_language, instrument_form, splitcol):

        instrument_string = '_'.join([instrument_language, instrument_form])
        instrument_model = getattr(instruments.models, instrument_string)

        import_helper = ImportHelper(dataset_file, instrument_model, splitcol)
        import_helper.import_data()

        instruments_map = InstrumentsMap.objects.get(language=instrument_language, form=instrument_form)

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

            # Create the instrument and the administration here.
            instrument_obj = instrument_model.objects.create()
            administration = Administration.objects.create(child=children[i],
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