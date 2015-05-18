import json
from django.core.management.base import BaseCommand
from instruments.import_dataset import import_dataset


# imports all datasets for a given instrument (language and form)
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', type=str)
        parser.add_argument('-f', '--form', type=str)
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):

        datasets = json.load(open('static/json/datasets.json'))

        if options['language'] and options['form']:
            input_language, input_form = options['language'], options['form']
            input_datasets = filter(lambda dataset: dataset['instrument_language'] == input_language and
                                                    dataset['instrument_form'] == input_form,
                                    datasets)
        elif options['file']:
            input_file = options['file']
            input_datasets = filter(lambda dataset: dataset['file'] == input_file,
                                    datasets)
        else:
            input_datasets = datasets


        for dataset in input_datasets:

            dataset_name = dataset['name']
            dataset_dataset = dataset['dataset']
            dataset_file = dataset['file']
            splitcol = dataset['splitcol']
            instrument_language = dataset['instrument_language']
            instrument_form = dataset['instrument_form']

            print "    Importing dataset", instrument_language, instrument_form, dataset_name, dataset_dataset
            import_dataset(dataset_name, dataset_dataset, dataset_file,
                           instrument_language, instrument_form, splitcol)