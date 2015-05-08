import xlrd
import codecs
import json
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', type=str)
        parser.add_argument('-f', '--form', type=str)

    def handle(self, *args, **options):

        instruments = json.load(open('static/json/instruments.json'))

        if options['language'] and options['form']:
            input_language, input_form = options['language'], options['form']
            input_instruments = filter(lambda instrument: instrument['language'] == input_language and
                                                          instrument['form'] == input_form,
                                       instruments)
            models_file = open('instruments/models.py', 'a')
        else:
            input_instruments = instruments
            models_file = open('instruments/models.py', 'w')

        for instrument in input_instruments:

            instr = '_'.join(instrument['language'].split() + [instrument['form']])
            models_file.write('from schemas.%s import *\n' % (instr))
            instrument_file = open('instruments/schemas/%s.py' % (instr), 'w')

            instrument_file.write('from django.db import models\n')
            instrument_file.write('from instruments.base import BaseTable\n')

            ftype = instrument['file'].split('.')[-1]

            if ftype == 'xlsx' or ftype == 'xls':
                sheet = xlrd.open_workbook(instrument['file']).sheet_by_index(0)
                col_names = list(sheet.row_values(0))
                nrows = sheet.nrows
                get_row = lambda row: list(sheet.row_values(row))
            elif ftype == 'csv':
                contents = [field for field in [line.split(',')
                                                for line in codecs.open(instrument['file'],
                                                                        encoding='utf-8').read().split('\n')]]
                col_names = contents[0]
                nrows = len(contents)
                get_row = lambda row: contents[row]
            else:
                raise IOError("Instrument file must be xlsx, xls, or csv.")


            instrument_file.write('\n\nclass %s(BaseTable):\n' % instr)

            if nrows <= 1:
                instrument_file.write('    pass\n')

            for row in xrange(1, nrows):
                row_values = get_row(row)
                if len(row_values) > 1:
                    itemID = row_values[col_names.index('itemID')]
                    choices = row_values[col_names.index('choices')].split('; ')
                    max_length = max(len(c) for c in choices)
                    instrument_file.write('    %s_choices = %s\n' % (itemID, [(c,c) for c in choices]))
                    instrument_file.write(
                        '    %s = models.CharField(max_length=%s, choices=%s_choices, null=True)\n' % (itemID,
                                                                                                       max_length,
                                                                                                       itemID)
                    )

            instrument_file.close()

        models_file.close()
