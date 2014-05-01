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
    
    special_cols = ['id', 'birth', 'gender', 'cdiage', 'momed']
    special_col_map = {}
    col_names = list(sh.row_values(0))

    instruments_map = InstrumentsMap.objects.create(name='WS', language='english')

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
      instrument = WS.objects.create()
      administration = Administration.objects.create(child=child,
                                             instrument=instruments_map,
                                             data_id=instrument.pk,
                                             age=int(row_values[special_col_map['cdiage']]))
      start = False
      instrument_data = {}
      col_name_index = 0
      for value in row_values:
        if col_names[col_name_index] == 'baabaa':
          start = True
        if start:
          instrument_data['col_'+col_names[col_name_index]] = int(value)
        col_name_index = col_name_index + 1
      WS.objects.filter(pk=instrument.pk).update(**instrument_data)
