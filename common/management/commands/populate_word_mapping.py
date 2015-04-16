import xlrd
import codecs
import json
from django.core.management.base import NoArgsCommand
from common.models import *


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instruments = json.load(open('static/json/instruments.json'))

        for instrument in instruments:

            instrument_language, instrument_form = instrument['language'], instrument['form']
            instrument_key = InstrumentsMap.objects.get(form=instrument_form, language=instrument_language)
            print "    Populating items for", instrument_language, instrument_form

            ftype = instrument['file'].split('.')[-1]

            if ftype == 'xlsx' or ftype == 'xls':
                sheet = xlrd.open_workbook(instrument['file']).sheet_by_index(0)
                col_names = list(sheet.row_values(0))
                nrows = sheet.nrows
                get_row = lambda row: list(sheet.row_values(row))
            elif ftype == 'csv':
                contents = [field for field in [line.split(',')
                                                for line in codecs.open(instrument['file'],
                                                                        encoding='utf-8').read().split('\n')]]
                col_names = contents[0]
                nrows = len(contents)
                get_row = lambda row: contents[row]
            else:
                raise IOError("Instrument file must be xlsx, xls, or csv.")

            for row in xrange(1, nrows):

                row_values = get_row(row)
                if len(row_values) > 1:
                    itemID = row_values[col_names.index('itemID')]
                    item = row_values[col_names.index('item')]
                    item_type = row_values[col_names.index('type')]
                    item_category = row_values[col_names.index('category')]
                    category_key = None
                    if item_type == 'word':
                        category_key = Category.objects.get(name = item_category)

                    #lang_lemma = row_values[col_names.index('lang_lemma')]
                    #uni_lemma = row_values[col_names.index('uni_lemma')]
                    definition = row_values[col_names.index('definition')]
                    gloss = row_values[col_names.index('gloss')]
                    #lexical_category = row_values[col_names.index('lexical_category')]
                    complexity_category = row_values[col_names.index('complexity_category')]

                    #if not WordInfo.objects.filter(uni_lemma=uni_lemma, lang_lemma=lang_lemma).exists():
                    #    WordInfo.objects.create(uni_lemma=uni_lemma, lang_lemma=lang_lemma)
                    #word_info = WordInfo.objects.get(uni_lemma=uni_lemma, lang_lemma=lang_lemma)

                    if not WordMapping.objects.filter(item_id=itemID, instrument=instrument_key).exists():
                        WordMapping.objects.create(item=item,
                                                   item_id=itemID,
                                                   instrument=instrument_key,
                                                   type=item_type,
                                                   category=category_key,
                                                   #word_info=word_info,
                                                   definition=definition,
#                                                   gloss=gloss,
    #                                               lexical_category=lexical_category,
                                                   complexity_category=complexity_category)
