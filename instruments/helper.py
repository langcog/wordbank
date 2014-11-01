from common.models import *
from instruments.models import *

def aggregate(admin_query=None):
  data = []
  if admin_query == None:
    administrations = Administration.objects.all()
  else:
    administrations = admin_query
  for administration in administrations:
    obj = {'age': administration.age if administration.age is not None else -1,
           #'date_of_test': administration.date_of_test if administration.date_of_test != None else datetime.datetime.now(),
           'gender': administration.child.gender if administration.child.gender else '?',
           #'date_of_birth': administration.child.date_of_birth if administration.child.date_of_birth != None else datetime.datetime.now(),
           'mom_ed': administration.child.mom_ed if administration.child.mom_ed else -1,  
           'source': administration.source.name if administration.source else 'Unknown',
           'citation': administration.source.citation if administration.source else 'Unknown',  
           'ethnicity': administration.child.ethnicity.ethnicity if administration.child.ethnicity != None else 'Unknown'}
    instrument = administration.instrument.name
    for subclass in BaseTable.__subclasses__():
      if instrument == subclass.__name__:
        instrument_class = subclass
        obj['instrument'] = instrument
        break
    instrument_obj = instrument_class.objects.get(pk=administration.data_id).__dict__
    production = 0
    comprehension = 0
    for field in instrument_class._meta.fields:
      field_name = field.get_attname_column()[0]
      if field_name.startswith('col_'):
        production_temp, comprehension_temp = get_production_comprehension_vals(instrument, instrument_obj[field_name])
        production = production + production_temp
        comprehension = comprehension + comprehension_temp
      if instrument == 'WS' and field_name == 'col_connthen':
        break
      if instrument == 'WG' and field_name == 'col_some':
        break
    obj['production'] = production
    obj['comprehension'] = comprehension
    data.append(obj)
  return data


def get_production_comprehension_vals(instrument_name, val):
  if val == None:
    val = 0
  if instrument_name == 'WS':
    production = val
    comprehension = val
  elif instrument_name == 'WG':
    comprehension = 1 if val > 0 else 0
    production = 1 if val == 2 else 0
  return (production, comprehension)

def search(request):
  admins = Administration.objects.all()
  instrument_class = WS
  if 'instrument' in request:
    admins = admins.filter(instrument__name=request['instrument'])
    for subclass in BaseTable.__subclasses__():
      if request['instrument'] == subclass.__name__:
        instrument_class = subclass
  if 'source_name' in request:
    admins = admins.filter(source__name=request['source_name'])
  if 'gender' in request:
    if 'M' in request['gender'] and 'F' not in  request['gender']:
      admins.filter(gender = 'M')
    elif 'M' not in request['gender'] and 'F' in  request['gender']:
      admins.filter(gender = 'F')
  if 'data_age1' in request:
    q = (request['data_age1'])
    if q is not None and q != '':
      admins = admins.filter(age__gte=int(request['data_age1']))
  if 'data_age2' in request:
    q = (request['data_age2'])
    if q is not None and q != '':
      admins = admins.filter(age__lte=int(request['data_age2']))
  return admins, instrument_class 

def createCSV(writer, admins, instrument_class):
  header = ['study_id', 'gender', 'date of birth', 'age', 'mom_ed', 'ethnicity', 'source', 'date of test']
  field_names = []
  for field in instrument_class._meta.fields:
    field_name = field.get_attname_column()[0]
    if not field_name.startswith('col_'):
      continue
    header.append(field_name[4:])
    field_names.append(field_name)
  writer.writerow(header)
  for admin in list(admins):
    row = []
    row.append(admin.child.study_id)
    row.append(admin.child.gender)
    row.append(admin.child.date_of_birth)
    row.append(admin.age)
    row.append(admin.child.mom_ed)
    row.append(admin.child.ethnicity)
    row.append(admin.source.name)
    if not instrument_class.objects.filter(pk=admin.data_id).exists():
      continue
    obj = instrument_class.objects.get(pk=admin.data_id).__dict__
    for field_name in field_names:
      row.append(obj[field_name])
    writer.writerow(row)
