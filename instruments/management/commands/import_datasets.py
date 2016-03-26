import json
from django.core.management.base import BaseCommand
from instruments.import_dataset import import_dataset


# Given no arguments, imports all datasets in 'static/json/datasets.json'.
# Given a language with -l and a form with -f imports datasets in 'static/json/datasets.json' that have the matching
# `instrument_language` and `instrument_form`.
# Given a file with --file, imports the dataset in 'static/json/datasets.json' that has the matching `file`.
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
            if not input_datasets:
                raise IOError("the specified language and form don't correspond to any datasets")
        elif options['file']:
            input_file = options['file']
            input_datasets = filter(lambda dataset: dataset['file'] == input_file,
                                    datasets)
            if not input_datasets:
                raise IOError("the specified file doesn't correspond to any datasets")
        else:
            input_datasets = datasets


        for dataset in input_datasets:

            dataset_name = dataset['name']
            dataset_dataset = dataset['dataset']
            dataset_file = dataset['file']
            splitcol = dataset['splitcol']
            norming = dataset['norming']
            if 'date_format' in dataset:
                date_format = dataset['date_format']
            else:
                date_format = None
            instrument_language = dataset['instrument_language']
            instrument_form = dataset['instrument_form']

            print "    Importing dataset", instrument_language, instrument_form, dataset_name, dataset_dataset
            import_dataset(dataset_name, dataset_dataset, dataset_file, instrument_language, instrument_form, splitcol, norming, date_format)
