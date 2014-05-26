from django.core.management.base import NoArgsCommand
import xlrd
import datetime
from common.models import *
from instruments.models import *

class Command(NoArgsCommand):

  def format_date(self, date_str):
    return datetime.datetime.strptime(date_str, '%m/%d/%Y')

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
    book = xlrd.open_workbook(args[0])

    sh = book.sheet_by_index(0)
    nrows = sh.nrows
    ncols = sh.ncols
    
    special_cols = ['id', 'gender', 'birth', 'cdiage', 'momed', 'DateOfBirth', 'DateOfCDI', 'source', 'ethnic']
    special_col_map = {}
    col_names = list(sh.row_values(0))

    instruments_map = InstrumentsMap.objects.create(name='WG', language='english')

    for special_col in special_cols:
      for index, value in enumerate(col_names):
        if value.lower() == special_col.lower():
          special_col_map[special_col] = index
          break

    for row in range(1, nrows):
      row_values = list(sh.row_values(row))
      child = Child.objects.create(study_id=row_values[special_col_map['id']])
      if 'DateOfBirth' in special_col_map and row_values[special_col_map['DateOfBirth']] != '':
        if type(row_values[special_col_map['DateOfBirth']]) == float:
          child.date_of_birth = datetime.datetime(1899,12,30) + datetime.timedelta(days=int(row_values[special_col_map['DateOfBirth']]))
        else:
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
      child.save()

      # Create the instrument and the administration here.
      instrument = WG.objects.create()
      administration = Administration.objects.create(child=child,
                                             instrument=instruments_map,
                                             data_id=instrument.pk,
                                             date_of_test=self.format_date(row_values[special_col_map['DateOfCDI']]))
      if 'cdiage' in special_col_map and row_values[special_col_map['cdiage']] != '':
        administration.age = int(row_values[special_col_map['cdiage']]) 
      if 'source' in special_col_map and row_values[special_col_map['source']] != '':
        source_num = int(row_values[special_col_map['source']])
        if Source.objects.filter(id=source_num+1).exists():
          administration.source = Source.objects.get(id=source_num+1)
      administration.save()

      # Parse all the fields for the given data entry here.
      start = False
      instrument_data = {}
      index = 0
      while index < ncols:
        if col_names[index] == 'baabaap':
          start = True
        if start:
          (name, offset) = self.extract_base(index, col_names)
          try:
            if offset == 2:
              value = int(row_values[index]) + int(row_values[index+1])
            else:
              value = int(row_values[index])
          except:
            value = 0
          instrument_data['col_'+name] = value
          index = index + offset
        else:
          index = index + 1
      WG.objects.filter(pk=instrument.pk).update(**instrument_data)
