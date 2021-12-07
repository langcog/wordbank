import string
from django.contrib.contenttypes.models import ContentType

from common.models import *
import instruments.models
from instruments import import_dataset_helper


# Given a datasets's name (ex Marchman), dataset (ex Norming), language (ex English), instrument (ex WS), splitcol bool.
# Uses import_dataset_helper to retrieve the data from that dataset's data file, using its field and value mappings.
# Creates Child and Administration objects for the entries in the resulting data.
def import_dataset(dataset_name, dataset_dataset, dataset_file, instrument_language, instrument_form, splitcol, norming, date_format, dataset_origin):

        var_safe = lambda s: ''.join([c for c in '_'.join(s.split()) if c in string.ascii_letters + '_'])
        instrument_string = var_safe(instrument_language) + '_' + var_safe(instrument_form)
        try:
            instrument_model = getattr(instruments.models, instrument_string)
        except AttributeError:
            raise IOError("instrument %s has no model defined" % instrument_string)

        import_helper = import_dataset_helper.ImportHelper(dataset_file, date_format, norming, splitcol)
        import_helper.import_data()

        instruments_map = Instrument.objects.get(language=instrument_language, form=instrument_form)

        children = {}

        for i, child_data in import_helper.children.items():
            # initialize the Child here
            child, created = Child.objects.get_or_create(study_internal_id=child_data['study_id'], dataset_origin=DatasetOrigin.objects.get(dataset_origin_name=dataset_origin))
            child.date_of_birth = child_data['date_of_birth']
            child.sex = child_data['sex']
            child.birth_order = child_data['birth_order']
            if child_data['momed'] is not None:
                child.caregiver_education = CaregiverEducation.objects.get(education_level__iexact = child_data['momed'])
            child.study_internal_caregiver_education = child_data['study_momed']
            child.ethnicity = child_data['ethnicity']

            children[i] = child
            child.save()
            if 'condition' in child_data:
                for condition in child_data['condition']:
                    c, created = HealthCondition.objects.get_or_create(health_condition_name=condition)
                    child.health_conditions.add(c)
                    pass
        
        for i, administration_data in import_helper.administrations.items():          
            administration, created = Administration.objects.get_or_create(child=children[i],
                                                           is_norming=administration_data['norming'],
                                                           date_of_test=administration_data['date_of_test'],
                                                           instrument=instruments_map,
                                                           age=administration_data['age'],
                                                           study_internal_age=administration_data['data_age'])

            administration.dataset = Dataset.objects.get(dataset_name=dataset_name,
                                                      instrument=instruments_map)

            if not administration.data_id:
                instrument_obj = instrument_model.objects.create()
                administration.data_id=instrument_obj.pk
                administration.data_content_type=ContentType.objects.get(app_label='instruments', model=instrument_string)
            else:
                instrument_obj = instrument_model.objects.get(id=administration.data_id)

            instrument_model.objects.filter(pk=instrument_obj.pk).update(**administration_data['item_data'])

            administration.save()
            if 'language' in administration_data:
                for language in administration_data['language']:
                    lang, prop, age = language.split(';')
                    try:
                        if not int(age): age = None
                    except:
                        age = None
                    l, created = LanguageExposure.objects.get_or_create(
                        administration=administration,
                        language=lang,
                        exposure_proportion=prop,
                        age_of_first_exposure=age
                        )