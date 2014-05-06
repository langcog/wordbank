from django.core.management.base import NoArgsCommand
import xlrd

class Command(NoArgsCommand):

  def extract_base(self, index, col_names):
    if index == len(col_names)-1:
      return (col_names[index], 1)
    col1 = col_names[index]
    col2 = col_names[index+1]
    if col1[0:len(col1)-1] == col2[0:len(col2)-1] and \
      (col1[len(col1)-1] == 'p' and col2[len(col2)-1] == 'u' or \
      col2[len(col2)-1] == 'u' and col2[len(col2)-1] == 'p'):
      base = col1[0:len(col1)-1]
      index = 2
    elif col1[1:] == col2[1:] and \
      (col1[0] == 'p' and col2[0] == 'u' or \
      col2[0] == 'u' and col2[0] == 'p'):
      base = col1[1:]
      index = 2
    else:
      base = col1
      index = 1
    return (base, index)

  def handle(self, *args, **options):
    book = xlrd.open_workbook('raw_data/CDI-WG.xlsx')

    sh = book.sheet_by_index(0)
    nrows = sh.nrows
    ncols = sh.ncols
    col_names = list(sh.row_values(0))
    
    f = open('instruments/wg.py', 'w')
    f.write('from django.db import models\n')
    f.write('\nclass WG(BaseTable):\n')
    start = False
    index = 0
    while index < ncols:
      if col_names[index] == 'baabaap':
        start = True
      (name, offset) = self.extract_base(index, col_names)
      if start:
        f.write('  col_' + name + ' = models.IntegerField(null=True, blank=True)\n')
        index = index + offset
      else:
        index = index + 1
    f.close()
