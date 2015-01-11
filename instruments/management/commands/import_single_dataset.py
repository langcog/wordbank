import json
from django.core.management.base import NoArgsCommand
from import_dataset import import_dataset


# imports a single dataset given its filename
# dataset filename must be in static/json/datasets.json
class Command(NoArgsCommand):

    def handle(self, *args, **options):

        dataset_file = args[0]
        datasets = json.load(open('static/json/datasets.json'))

        for dataset in datasets:

            if dataset['file'] == dataset_file:

                dataset_name = dataset['name']
                dataset_dataset = dataset['dataset']
                splitcol = dataset['splitcol']
                instrument_language = dataset['instrument_language']
                instrument_form = dataset['instrument_form']

                print "    Importing dataset", instrument_language, instrument_form, dataset_name, dataset_dataset
                import_dataset(dataset_name, dataset_dataset, dataset_file,
                               instrument_language, instrument_form, splitcol)

                break