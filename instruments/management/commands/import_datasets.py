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

        if options['language'] or options['form']:
            filter_exps = []
            if options['language']:
                input_language = options['language']
                filter_exps.append("dataset['instrument_language'] == '%s'" % input_language)

            if options['form']:
                input_form = options['form']
                filter_exps.append("dataset['instrument_form'] == '%s'" % input_form)

            combined_exps = ' and '.join(filter_exps)

            input_datasets = [dataset for dataset in datasets if eval(combined_exps)]
            
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

            print("    Importing dataset", instrument_language, instrument_form, dataset_name, dataset_dataset)
            import_dataset(dataset_name, dataset_dataset, dataset_file, instrument_language, instrument_form, splitcol, norming, date_format)
