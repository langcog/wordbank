from django.core.management.base import NoArgsCommand
from common.models import *
from datetime import datetime
from instruments.models import *

import xlrd

class Command(NoArgsCommand):
  
  def format_date(self, date_str):
    return datetime.strptime(date_str, '%m/%d/%Y')
 
  def handle(self, *args, **options):
    # Name of the CDI file is here.
    book = xlrd.open_workbook('raw_data/CDI-WS-2.xlsx')

    sh = book.sheet_by_index(0)
    nrows = sh.nrows
    ncols = sh.ncols
    
    special_cols = ['id', 'birth', 'gender', 'cdiage', 'momed', 'DateOfBirth', 'DateOfCDI', 'source', 'ethnic']
    special_col_map = {}
    col_names = list(sh.row_values(0))

    instruments_map = InstrumentsMap.objects.get(name='WS', language='english')

    for special_col in special_cols:
      for index, value in enumerate(col_names):
        if value.lower() == special_col.lower():
          special_col_map[special_col] = index
          break
    
    for row in range(1, nrows):
      row_values = list(sh.row_values(row))
      
      # Initialize the Child here.
      child = Child.objects.create(study_id=row_values[special_col_map['id']])
      if 'DateOfBirth' in special_col_map and row_values[special_col_map['DateOfBirth']] != '':
        child.date_of_birth = self.format_date(row_values[special_col_map['DateOfBirth']])
      if 'gender' in special_col_map and row_values[special_col_map['gender']] != '':
        child.gender = row_values[special_col_map['gender']]
      if 'birth' in special_col_map and row_values[special_col_map['birth']] != '':
        child.birth_order = int(row_values[special_col_map['birth']])
      if 'momed' in special_col_map and row_values[special_col_map['momed']] != '':
        child.mom_ed = int(row_values[special_col_map['momed']])
      if 'ethnic' in special_col_map and row_values[special_col_map['ethnic']] != '':
        ethnic_num = int(row_values[special_col_map['ethnic']])
        if Ethnicity.objects.filter(id=ethnic_num).exists():
          child.ethnicity = Ethnicity.objects.get(pk=ethnic_num)
      if 'source' in special_col_map and row_values[special_col_map['source']] != '':
        source_num = int(row_values[special_col_map['source']])
        if Source.objects.filter(id=source_num+1).exists():
          child.source = Source.objects.get(id=source_num+1)
      child.save()
      
      # Create the instrument and the administration here.
      instrument = WS.objects.create()
      administration = Administration.objects.create(child=child,
                                             instrument=instruments_map,
                                             data_id=instrument.pk,
                                             date_of_test=self.format_date(row_values[special_col_map['DateOfCDI']]))
      if 'cdiage' in special_col_map and row_values[special_col_map['cdiage']] != '':
        administration.age = int(row_values[special_col_map['cdiage']]) 
        administration.save()

      # Parse all the fields for the given data entry here.
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
