from common.models import *
from models import *


def aggregate(admin_query=None):

    data = []

    if not admin_query:
        administrations = Administration.objects.all()
    else:
        administrations = admin_query

    for administration in administrations:
        obj = {'age': administration.age if administration.age is not None else -1,
               #'date_of_test': administration.date_of_test if administration.date_of_test != None else datetime.datetime.now(),
               'sex': administration.child.sex if administration.child.sex else '?',
               #'date_of_birth': administration.child.date_of_birth if administration.child.date_of_birth != None else datetime.datetime.now(),
               'mom_ed': administration.child.mom_ed if administration.child.mom_ed else -1,
               'source': administration.source.name if administration.source else 'Unknown',
#               'citation': administration.source.citation if administration.source else 'Unknown',
               'ethnicity': administration.child.ethnicity.ethnicity if administration.child.ethnicity else 'Unknown'}
        instrument_type = administration.instrument.form
        instrument_language = administration.instrument.language
        for subclass in BaseTable.__subclasses__():
            if '_'.join([instrument_language, instrument_type]) == subclass.__name__:
                instrument_class = subclass
                obj['instrument'] = instrument_type
                break
        instrument_obj = instrument_class.objects.get(pk=administration.data_id).__dict__
        production = None
        comprehension = None
        for field in instrument_class._meta.fields:
            field_name = field.get_attname_column()[0]
            if field_name.startswith('item_'):
                production_temp, comprehension_temp = get_production_comprehension_vals(instrument_type, instrument_obj[field_name])
                production = production_temp
                comprehension = comprehension_temp
        obj['production'] = production
        obj['comprehension'] = comprehension
        data.append(obj)
    return data


def get_production_comprehension_vals(instrument_type, val):
    if not val:
        val = 0
    if instrument_type == 'WS':
        production = val
        comprehension = val
    elif instrument_type == 'WG':
        comprehension = 1 if val > 0 else 0
        production = 1 if val == 2 else 0
    else:
        raise RuntimeError("invalid instrument type")
    return production, comprehension


'''
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
        if 'M' in request['gender'] and 'F' not in request['gender']:
            admins.filter(gender='M')
        elif 'M' not in request['gender'] and 'F' in request['gender']:
            admins.filter(gender='F')
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
        if admin.child.ethnicity is not None:
            row.append(admin.child.ethnicity.ethnicity)
        else:
            row.append('unknown')
        row.append(admin.source.name)
        row.append(admin.date_of_test)
        if not instrument_class.objects.filter(pk=admin.data_id).exists():
            continue
        obj = instrument_class.objects.get(pk=admin.data_id).__dict__
        for field_name in field_names:
            row.append(obj[field_name])
        writer.writerow(row)
'''