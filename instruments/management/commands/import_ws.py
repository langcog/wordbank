from django.core.management.base import NoArgsCommand
import xlrd
from common.models import *
from instruments.models import *

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    book = xlrd.open_workbook('raw_data/CDI-WS.xlsx')

    sh = book.sheet_by_index(0)
    nrows = sh.nrows
    ncols = sh.ncols
    
    start = False
    for value in sh.row_values(0):
      if value == 'baabaa':
        start = True
      if start:
        f.write('  _' + value + ' = models.IntegerField()\n')
