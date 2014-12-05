from django.core.management.base import NoArgsCommand
from common.models import *
import xlrd


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instruments = open('raw_data/instruments.txt', 'r').read().split('\n')
        instruments = filter(lambda i: i != '', instruments)

        for instrument in instruments:

            instrument_language, instrument_name = instrument.split('_')
            instruments_map = InstrumentsMap.objects.get(name=instrument_name, language=instrument_language)

            book = xlrd.open_workbook('raw_data/%s/[%s].xlsx' % (instrument, instrument))

            sheet = book.sheet_by_index(0)
            col_names = list(sheet.row_values(0))

            for row in xrange(1, sheet.nrows):

                row_values = list(sheet.row_values(row))
                item_type = row_values[col_names.index('type')]

                if item_type == 'word':

                    item = row_values[col_names.index('item')]
                    category = row_values[col_names.index('category')]
                    lang_lemma = row_values[col_names.index('lang_lemma')]
                    uni_lemma = row_values[col_names.index('uni_lemma')]
                    definition = row_values[col_names.index('definition')]

                    if not WordInfo.objects.filter(uni_lemma=uni_lemma, lang_lemma=lang_lemma).exists():
                        WordInfo.objects.create(uni_lemma=uni_lemma, lang_lemma=lang_lemma)
                    word_info = WordInfo.objects.get(uni_lemma=uni_lemma, lang_lemma=lang_lemma)

                    WordMapping.objects.create(item=item,
                                               definition=definition,
                                               category=category,
                                               instrument=instruments_map,
                                               word_info=word_info)