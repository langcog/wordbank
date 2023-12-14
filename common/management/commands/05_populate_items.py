import xlrd, json, csv
from django.core.management.base import BaseCommand
from common.models import *


# Populates the Item and UniLemma models with data from instrument definition files.
# Given no arguments, does so for all instruments in 'static/json/instruments.json'.
# Given a language with -l and a form with -f, does so for only their Instrument object.


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [cell for cell in row]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-l", "--language", type=str)
        parser.add_argument("-f", "--form", type=str)

    def handle(self, *args, **options):
        instruments = json.load(open("static/json/instruments.json"))

        if options["language"] or options["form"]:
            filter_exps = []
            if options["language"]:
                input_language = options["language"]
                filter_exps.append("instrument['language'] == '%s'" % input_language)

            if options["form"]:
                input_form = options["form"]
                filter_exps.append("instrument['form'] == '%s'" % input_form)

            combined_exps = " and ".join(filter_exps)

            input_instruments = [
                instrument for instrument in instruments if eval(combined_exps)
            ]

        else:
            input_instruments = instruments

        for instrument in input_instruments:
            instrument_language, instrument_form = (
                instrument["language"],
                instrument["form"],
            )
            instrument_obj = Instrument.objects.get(
                form=instrument_form, language=instrument_language
            )
            print("    Populating items for", instrument_language, instrument_form)

            ftype = instrument["file"].split(".")[-1]

            if ftype == "xlsx" or ftype == "xls":
                sheet = xlrd.open_workbook(instrument["file"]).sheet_by_index(0)
                col_names = list(sheet.row_values(0))
                nrows = sheet.nrows
                get_row = lambda row: list(sheet.row_values(row))
            elif ftype == "csv":
                contents = list(
                    unicode_csv_reader(open(instrument["file"], encoding="utf-8-sig"))
                )
                col_names = contents[0]
                nrows = len(contents)
                get_row = lambda row: contents[row]
            else:
                raise IOError("Instrument file must be xlsx, xls, or csv.")

            for row in range(1, nrows):
                row_values = get_row(row)
                if len(row_values) > 1:
                    itemID = row_values[col_names.index("itemID")]
                    study_internal_item = row_values[col_names.index("item")]
                    item_kind = row_values[col_names.index("type")]

                    item_category = row_values[col_names.index("category")]
                    if item_kind == "word" and not item_category in ["", 'NA']:
                        try:
                            item_category = ItemCategory.objects.get(
                                category=item_category
                            )
                        except:
                            raise IOError(
                                "Can't find category %s in model" % (item_category,)
                            )
                    else:
                        item_category = None

                    item_definition = row_values[col_names.index("definition")]
                    english_gloss = row_values[col_names.index("gloss")]

                    # TODO category complexity is moved to ItemCategory model
                    if "complexity_category" in col_names:
                        complexity_category = row_values[
                            col_names.index("complexity_category")
                        ]
                    else:
                        complexity_category = None

                    if "uni_lemma" in col_names:
                        uni_lemma = row_values[col_names.index("uni_lemma")]
                        if uni_lemma == "":
                            item_map = None
                        else:
                            if not UniLemma.objects.filter(
                                uni_lemma=uni_lemma
                            ).exists():
                                UniLemma.objects.create(uni_lemma=uni_lemma)
                            item_map = UniLemma.objects.get(uni_lemma=uni_lemma)

                    else:
                        item_map = None

                    data_dict = {
                        "study_internal_item": study_internal_item,
                        "item_kind": item_kind,
                        "item_category": item_category,
                        "uni_lemma": item_map,
                        "item_definition": item_definition,
                        "english_gloss": english_gloss,
                    }
                    cdi_item, created = Item.objects.update_or_create(
                        item_id=itemID, instrument=instrument_obj, defaults=data_dict
                    )

            all_words = Item.objects.filter(
                instrument_id=instrument_obj, item_kind="word"
            )
            all_matched = all_words.exclude(
                uni_lemma_id__isnull=True
            )  # .exclude(uni_lemma_id__exact='')
            if all_words.count() > 0:
                lemma_coverage = round(
                    float(all_matched.count()) / float(all_words.count()), 2
                )
            else:
                lemma_coverage = 0
            instrument_obj.unilemma_coverage = lemma_coverage
            instrument_obj.save()
