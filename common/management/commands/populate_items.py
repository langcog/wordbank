import xlrd
import codecs
import json
import re
from django.core.management.base import BaseCommand
from common.models import *
import csv


# Populates the ItemInfo and ItemMap models with data from instrument definition files.
# Given no arguments, does so for all instruments in 'static/json/instruments.json'.
# Given a language with -l and a form with -f, does so for only their Instrument object.

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]
        
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', type=str)
        parser.add_argument('-f', '--form', type=str)

    def handle(self, *args, **options):

        instruments = json.load(open('static/json/instruments.json'))

        if options['language'] and options['form']:
            input_language, input_form = options['language'], options['form']
            input_instruments = filter(lambda instrument: instrument['language'] == input_language and
                                                          instrument['form'] == input_form,
                                       instruments)
        else:
            input_instruments = instruments

        for instrument in input_instruments:

            instrument_language, instrument_form = instrument['language'], instrument['form']
            instrument_obj = Instrument.objects.get(form=instrument_form, language=instrument_language)
            print "    Populating items for", instrument_language, instrument_form

            ftype = instrument['file'].split('.')[-1]

            if ftype == 'xlsx' or ftype == 'xls':
                sheet = xlrd.open_workbook(instrument['file']).sheet_by_index(0)
                col_names = list(sheet.row_values(0))
                nrows = sheet.nrows
                get_row = lambda row: list(sheet.row_values(row))
            elif ftype == 'csv':
                # contents = [[field.replace('"', '') for field in row] for row in [line.split(',')
                #                                 for line in re.split("\n|\r", codecs.open(instrument['file'],
                #                                                                           encoding='utf-8').read())]]

                contents = list(unicode_csv_reader(open(instrument['file'])))
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
                    if item_type == 'word' and item_category != "":
                        try:
                            category_key = Category.objects.get(name = item_category)
                        except:
                            raise IOError("Can't find category %s in model" % (item_category,))

                    definition = row_values[col_names.index('definition')]
                    gloss = row_values[col_names.index('gloss')]
                    if 'complexity_category' in col_names:
                        complexity_category = row_values[col_names.index('complexity_category')]
                    else:
                        complexity_category = None

                    if 'uni_lemma' in col_names:
                        uni_lemma = row_values[col_names.index('uni_lemma')]
                        if uni_lemma == "":
                            item_map = None
                        else:
                            if not ItemMap.objects.filter(uni_lemma=uni_lemma).exists():
                                ItemMap.objects.create(uni_lemma=uni_lemma)
                            item_map = ItemMap.objects.get(uni_lemma=uni_lemma)

                    else:
                        item_map = None

                    data_dict = {'item': item,
                                 'type': item_type,
                                 'category': category_key,
                                 'map': item_map,
                                 'definition': definition,
                                 'gloss': gloss,
                                 'complexity_category': complexity_category}

                    if not ItemInfo.objects.filter(item_id=itemID, instrument=instrument_obj).exists():
                        ItemInfo.objects.create(item_id=itemID, instrument=instrument_obj)
                    ItemInfo.objects.filter(item_id=itemID, instrument=instrument_obj).update(**data_dict)
