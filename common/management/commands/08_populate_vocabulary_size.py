import string
from django.core.management.base import BaseCommand
from common.models import *
import instruments.models


# Populates the production and comprehension fields of Administration objects with the number of items
# produced/comprehended by that object's data_id entry in the corresponding instruments model.
# Given no arguments, does so for all instruments in 'static/json/instruments.json'.
# Given a language with -l and a form with -f, does so for only their Instrument object.
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-l", "--language", type=str)
        parser.add_argument("-f", "--form", type=str)

    def update_admin(self, s):
        try:
            admin = Administration.objects.get(data_id=s.basetable_ptr_id)
        except Exception:
            print(f'No record found. Deleting {s}')
            s.delete()
            return
        #print (f'Processing {s} for administration {admin} with id {admin.id}, Production={s.production}; Comprehension={s.comprehension}')
        admin.production = s.production
        admin.comprehension = s.comprehension
        admin.save()

    def handle(self, *args, **options):
        if options["language"] or options["form"]:
            kwargs = {}

            if options["language"]:
                input_language = options["language"]
                kwargs["language"] = input_language

            if options["form"]:
                input_form = options["form"]
                kwargs["form"] = input_form

            input_instruments = Instrument.objects.filter(**kwargs)
        else:
            input_instruments = Instrument.objects.all()
            print(f'Total Instruments to process {Instrument.objects.count()}')

        for instrument in input_instruments:
            print(
                f"    {list(input_instruments).index(instrument)+1}. Caching vocabulary sizes for {instrument.language}, {instrument.form}"
            )

            var_safe = lambda s: "".join(
                [c for c in "_".join(s.split()) if c in string.ascii_letters + "_"]
            )
            instrument_string = (
                var_safe(instrument.language) + "_" + var_safe(instrument.form)
            )
            instrument_model = getattr(instruments.models, instrument_string)
            instrument_table = instrument_model._meta.db_table
            words = [
                item.item_id
                for item in Item.objects.filter(
                    instrument=instrument.pk, item_kind="word"
                )
            ]
            query = "select basetable_ptr_id, "

            prod_query = ""
            comp_query = ""
            if len(words) < 1:
                print(f'Doing nothing for {instrument}')
                continue
            for word in words:
                prod_query += f"case when {word}='produce' or {word}='produces' then 1 else 0 end + " 
                comp_query += f"case when {word}='produce' or {word}='produces' or {word}='underst' or {word}='understands' then 1 else 0 end + "

            prod_query = prod_query[:-2]
            prod_query += "as production, "

            comp_query = comp_query[:-2]
            comp_query += "as comprehension "
            query += prod_query
            query += comp_query
            query += "from %s;" % (instrument_table)
            
            sizes = list(instrument_model.objects.raw(query))
            #print (f'Processing {len(sizes)} records')

            

            for result in map(self.update_admin, sizes):
                pass
