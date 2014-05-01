from django.core.management.base import NoArgsCommand
import xlrd
from common.models import *
from instruments.models import *

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
      offset = 2
    elif col1[1:] == col2[1:] and \
      (col1[0] == 'p' and col2[0] == 'u' or \
      col2[0] == 'u' and col2[0] == 'p'):
      base = col1[1:]
      offset = 2
    else:
      base = col1
      offset = 1
    return (base, offset)


  def handle(self, *args, **options):
    book = xlrd.open_workbook('raw_data/CDI-WG.xlsx')

    sh = book.sheet_by_index(0)
    nrows = sh.nrows
    ncols = sh.ncols
    
    special_cols = ['id', 'gender', 'birth', 'cdiage', 'momed']
    special_col_map = {}
    col_names = list(sh.row_values(0))

    instruments_map = InstrumentsMap.objects.create(name='WG', language='english')

    for special_col in special_cols:
      for index, value in enumerate(col_names):
        if value.lower() == special_col:
          special_col_map[special_col] = index
          break
    
    for row in range(1, nrows):
      row_values = list(sh.row_values(row))
      child = Child.objects.create(gender=row_values[special_col_map['gender']],
                    study_id=row_values[special_col_map['id']],
                    birth_order=row_values[special_col_map['birth']],
                    mom_ed=int(row_values[special_col_map['momed']]))
      instrument = WG.objects.create()
      administration = Administration.objects.create(child=child,
                                             instrument=instruments_map,
                                             data_id=instrument.pk,
                                             age=int(row_values[special_col_map['cdiage']]))
      start = False
      instrument_data = {}
      index = 0
      while index < ncols:
        if col_names[index] == 'baabaap':
          start = True
        if start:
          (name, offset) = self.extract_base(index, col_names)
          if offset == 2:
            value = int(row_values[index]) + int(row_values[index+1])
          else:
            value = int(row_values[index])
          instrument_data['col_'+name] = value
          index = index + offset
        else:
          index = index + 1
      WG.objects.filter(pk=instrument.pk).update(**instrument_data)
