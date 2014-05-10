from common.models import *
from instruments.models import *

def aggregate():
  data = []
  administrations = Administration.objects.all()
  for administration in administrations: 
    obj = {'age': administration.age if administration.age is not None else -1,
           #'date_of_test': administration.date_of_test if administration.date_of_test != None else datetime.datetime.now(),
           'gender': administration.child.gender if administration.child.gender != None else 'U',
           #'date_of_birth': administration.child.date_of_birth if administration.child.date_of_birth != None else datetime.datetime.now(),
           'mom_ed': administration.child.mom_ed if administration.child.mom_ed != None else -1}  
    instrument = administration.instrument.name
    for subclass in BaseTable.__subclasses__():
      if instrument == subclass.__name__:
        instrument_class = subclass
        obj['instrument'] = instrument
        break
    instrument_obj = instrument_class.objects.get(pk=administration.data_id).__dict__
    total = 0
    for field in instrument_class._meta.fields:
      field_name = field.get_attname_column()[0]
      if field_name.startswith('col_'):
        total = total + instrument_obj[field_name]
    obj['total'] = total
    data.append(obj)
  return data
