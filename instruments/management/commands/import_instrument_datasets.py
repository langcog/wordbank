import json
from django.core.management.base import NoArgsCommand
from import_dataset import import_dataset


# imports all datasets for a given instrument (language and form)
class Command(NoArgsCommand):

    def handle(self, *args, **options):

        language, form = args[0], args[1]
        datasets = json.load(open('static/json/datasets.json'))

        for dataset in datasets:

            dataset_name = dataset['name']
            dataset_dataset = dataset['dataset']
            dataset_file = dataset['file']
            splitcol = dataset['splitcol']
            instrument_language = dataset['instrument_language']
            instrument_form = dataset['instrument_form']

            if instrument_language == language and instrument_form == form:

                print "    Importing dataset", instrument_language, instrument_form, dataset_name, dataset_dataset
                import_dataset(dataset_name, dataset_dataset, dataset_file,
                               instrument_language, instrument_form, splitcol)