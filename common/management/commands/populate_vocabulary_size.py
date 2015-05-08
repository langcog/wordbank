from django.core.management.base import NoArgsCommand
from common.models import *
import instruments.models

class Command(NoArgsCommand):

    def handle(self, *args, **options):

        if len(args) > 1:
            input_language, input_form = args[0], args[1]
            input_instruments = Instrument.objects.filter(language = input_language, form = input_form)
        else:
            input_instruments = Instrument.objects.all()

        for instrument in input_instruments:

            print "    Caching vocabulary sizes for", instrument.language, instrument.form

            instrument_model = getattr(instruments.models, '_'.join(instrument.language.split() + [instrument.form]))
            instrument_table = instrument_model._meta.db_table
            words = [item.item_id for item in ItemInfo.objects.filter(instrument = instrument.pk, type = 'word')]

            query = "select basetable_ptr_id, "

            prod_query = ''
            comp_query = ''
            for word in words:
                prod_query += "case when %s='produces' then 1 else 0 end + " % (word)
                comp_query += "case when %s='produces' or %s='understands' then 1 else 0 end + " % (word, word)

            prod_query = prod_query[:-2]
            prod_query += "as production, "

            comp_query = comp_query[:-2]
            comp_query += "as comprehension "
            query += prod_query
            query += comp_query
            query += "from %s;" % (instrument_table)

            sizes = instrument_model.objects.raw(query)
            def update_admin(s):
                admin = Administration.objects.get(data_id=s.basetable_ptr_id)
                admin.production = s.production
                admin.comprehension = s.comprehension
                admin.save()
            map(update_admin, sizes)
