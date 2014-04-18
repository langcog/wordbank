from django.core.management.base import NoArgsCommand
import xlrd

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    book = xlrd.open_workbook('raw_data/CDI-WS.xlsx')

    sh = book.sheet_by_index(0)
    nrows = sh.nrows
    ncols = sh.ncols
    
    f = open('instruments/ws.py', 'w')
    f.write('from django.db import models\n')
    f.write('\nclass WS:\n')
    start = False
    for value in sh.row_values(0):
      if value == 'baabaa':
        start = True
      if start:
        f.write('  _' + value + ' = models.IntegerField()\n')
