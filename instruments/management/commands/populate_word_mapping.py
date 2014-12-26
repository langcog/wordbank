import xlrd
import json
from django.core.management.base import NoArgsCommand
from common.models import *


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instruments = json.load(open('static/json/instruments.json'))

        for instrument in instruments:

            instrument_language, instrument_form = instrument['language'], instrument['form']
            instruments_map = InstrumentsMap.objects.get(form=instrument_form, language=instrument_language)
            print "    Populating items for", instrument_language, instrument_form
            book = xlrd.open_workbook(instrument['file'])

            sheet = book.sheet_by_index(0)
            col_names = list(sheet.row_values(0))

            for row in xrange(1, sheet.nrows):

                row_values = list(sheet.row_values(row))
                item = row_values[col_names.index('item')]
                item_type = row_values[col_names.index('type')]
                item_category = row_values[col_names.index('category')]

                lang_lemma = row_values[col_names.index('lang_lemma')]
                uni_lemma = row_values[col_names.index('uni_lemma')]
                definition = row_values[col_names.index('definition')]
                lexical_category = row_values[col_names.index('lexical_category')]

                if not WordInfo.objects.filter(uni_lemma=uni_lemma, lang_lemma=lang_lemma).exists():
                    WordInfo.objects.create(uni_lemma=uni_lemma, lang_lemma=lang_lemma)
                word_info = WordInfo.objects.get(uni_lemma=uni_lemma, lang_lemma=lang_lemma)

                WordMapping.objects.create(item=item,
                                           instrument=instruments_map,
                                           type=item_type,
                                           category=item_category,
                                           word_info=word_info,
                                           definition=definition,
                                           lexical_category=lexical_category)