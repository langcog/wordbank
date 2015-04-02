import xlrd
import json
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        f = open('instruments/models.py', 'a')
        instruments = json.load(open('static/json/instruments.json'))

        for instrument in instruments:

            instr = '_'.join([instrument['language'], instrument['form']])
            f.write('from %s import *\n' % (instr))
            instrument_file = open('instruments/%s.py' % (instr), 'w')

            instrument_file.write('from django.db import models\n')
            instrument_file.write('from base import BaseTable\n')

            book = xlrd.open_workbook(instrument['file'])

            sheet = book.sheet_by_index(0)
            nrows = sheet.nrows
            col_names = list(sheet.row_values(0))

            instrument_file.write('\n\nclass %s(BaseTable):\n' % instr)

            if nrows <= 1:
                instrument_file.write('    pass\n')

            for row in xrange(1, nrows):
                row_values = list(sheet.row_values(row))
                itemID = row_values[col_names.index('itemID')]
                choices = row_values[col_names.index('choices')].split(', ')
                instrument_file.write('    %s_choices = %s\n' % (itemID, [(c,c) for c in choices]))
                instrument_file.write('    %s = models.CharField(max_length=20, choices=%s_choices, null=True)\n' % (itemID, itemID))

            instrument_file.close()

        f.close()
