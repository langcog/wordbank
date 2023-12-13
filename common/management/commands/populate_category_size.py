from django.core.management.base import BaseCommand
from common.models import *
import instruments.models
from collections import defaultdict
from instruments.utils import get_instrument_model


# Populates the CategorySize objects with each data_id entry's Administration object and number of words
# produced/comprehended in each ItemCategory by that object's data_id entry in the corresponding instruments model.
# Given no arguments, does so for all instruments in 'static/json/instruments.json'.
# Given a language with -l and a form with -f, does so for only their Instrument object.
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-l", "--language", type=str)
        parser.add_argument("-f", "--form", type=str)

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

        for instrument in input_instruments:
            print(
                "    Caching category sizes for", instrument.language, instrument.form
            )

            instrument_model = get_instrument_model(
                instrument.language, instrument.form
            )
            instrument_table = instrument_model._meta.db_table
            all_words = Item.objects.filter(
                instrument=instrument.pk, type="word", category_id__isnull=False
            )  # isnull condition added for TEDS Twos

            category_words = defaultdict(list)
            for word in all_words:
                category_words[word.category.id].append(word.item_id)

            for category, words in category_words.items():
                query = "select basetable_ptr_id, "

                prod_query = ""
                comp_query = ""
                for word in words:
                    prod_query += "case when %s='produces' then 1 else 0 end + " % (
                        word
                    )
                    comp_query += (
                        "case when %s='produces' or %s='understands' then 1 else 0 end + "
                        % (word, word)
                    )

                prod_query = prod_query[:-2]
                prod_query += "as production, "

                comp_query = comp_query[:-2]
                comp_query += "as comprehension "

                query += prod_query
                query += comp_query
                query += "from %s;" % (instrument_table)

                sizes = instrument_model.objects.raw(query)

                def create_size(s):
                    cat = ItemCategory.objects.get(pk=category)
                    CategorySize.objects.create(
                        data_id=s.basetable_ptr_id,
                        item_category_id=cat,
                        production=s.production,
                        comprehension=s.comprehension,
                    )

                map(create_size, sizes)
