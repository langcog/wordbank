import os
from django.core.management.base import NoArgsCommand
from common.models import *
import instruments.models
from import_data_helper import ImportHelper


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        path_to_data_file = args[0]
        data_file = os.path.splitext(os.path.basename(path_to_data_file))[0]

        instrument = os.path.splitext(args[0])[0].split('/')[-2]
        instrument_model = getattr(instruments.models, instrument)

        import_helper = ImportHelper(path_to_data_file, data_file, instrument_model)
        import_helper.import_data()

        instrument_language, instrument_name = instrument.split('_')

        instruments_map = InstrumentsMap.objects.get(name=instrument_name, language=instrument_language)

        children = {}

        for i, child_data in import_helper.children.iteritems():

            # Initialize the Child here.
            child = Child.objects.create(study_id=child_data['study_id'])
            child.date_of_birth = child_data['date_of_birth']
            child.gender = child_data['gender']
            child.birth_order = child_data['birth_order']
            child.mom_ed = child_data['mom_ed']
            if Ethnicity.objects.filter(id=child_data['ethnic_num']).exists():
                child.ethnicity = Ethnicity.objects.get(pk=child_data['ethnic_num'])

            children[i] = child
            child.save()

        for i, administration_data in import_helper.administrations.iteritems():

            # Create the instrument and the administration here.
            instrument = instrument_model.objects.create()
            administration = Administration.objects.create(child=children[i],
                                                           date_of_test=administration_data['date_of_test'],
                                                           instrument=instruments_map,
                                                           data_id=instrument.pk,
                                                           age=administration_data['age'],
                                                           data_age=administration_data['data_age'])

            if Source.objects.filter(name=administration_data['source_name'],
                                     dataset=administration_data['source_dataset'],
                                     instrument=instrument).exists():
                administration.source = Source.objects.get(name=administration_data['source_name'],
                                                           dataset=administration_data['source_dataset'],
                                                           instrument=instrument)

            instrument_model.objects.filter(pk=instrument.pk).update(**administration_data['instrument_data'])

            administration.save()