from common.models import *
from models import *


def aggregate(admin_query=None):

    safe_field = lambda field: 'Unknown' if field is None or field == 'NULL' else field
    data = []

    if not admin_query:
        administrations = Administration.objects.all()
    else:
        administrations = admin_query

    for administration in administrations:
        if administration.child.momed_id is None:
            momed = None
        else:
            momed_obj = MomEd.objects.get(pk=administration.child.momed_id)
            momed = str(momed_obj.order) + '. ' + momed_obj.level
        if administration.child.birth_order is None:
            birth_order = None
        else:
            get_birth_order = lambda bo: {1: '1. First',
                                          2: '2. Second',
                                          3: '3. Third'}.get(bo, '4. Fourth or more')
            birth_order = get_birth_order(administration.child.birth_order)
        admin_obj = {'age': safe_field(administration.age),
               'sex': safe_field(administration.child.get_sex_display()),
               'mom_ed': safe_field(momed),
               'birth_order': safe_field(birth_order),
               'source': safe_field(administration.source.name),
               'ethnicity': safe_field(administration.child.get_ethnicity_display()),
               'language': safe_field(administration.instrument.language),
               'form': safe_field(administration.instrument.get_form_display())}
        data.append(admin_obj)
    return data