from django.core.management.base import NoArgsCommand
import xlrd

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    book = xlrd.open_workbook('raw_data/CDI-WG.xlsx')

    sh = book.sheet_by_index(0)
    nrows = sh.nrows
    ncols = sh.ncols
    
    f = open('instruments/wg.py', 'w')
    f.write('from django.db import models\n')
    f.write('\nclass WS(models.Model):\n')
    start = False
    base = ''
    for value in sh.row_values(0):
      if value == 'baabaap':
        start = True
      if 
      if start:
        f.write('  col_' + value + ' = models.IntegerField(null=True, blank=True)\n')
