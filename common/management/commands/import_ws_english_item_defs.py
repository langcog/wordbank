from django.core.management.base import NoArgsCommand
from common.models import *
from datetime import datetime

import xlrd

class Command(NoArgsCommand):
  
  def handle(self, *args, **options):
    # Name of the CDI file is here.
    book = xlrd.open_workbook('raw_data/WordsSentencesEnglishitemdefs.xlsx')

    sh = book.sheet_by_index(0)
    nrows = sh.nrows
    ncols = sh.ncols
    
    special_cols = ['ItemName', 'CatID', 'ItemDescription']
    special_col_map = {}
    col_names = list(sh.row_values(0))

    instruments_map = InstrumentsMap.objects.get(name='WS', language='english')

    for special_col in special_cols:
      for index, value in enumerate(col_names):
        if value == special_col:
          special_col_map[special_col] = index
          break
    
    for row in range(1, nrows):
      row_values = list(sh.row_values(row))
      
      # Parse all the fields for the given data entry here.
      catID = row_values[special_col_map['CatID']]
      item_name = row_values[special_col_map['ItemName']]
      item_description = row_values[special_col_map['ItemDescription']]

      if CDICategory.objects.filter(name=catID).exists():
        cdi_category = CDICategory.objects.get(name=catID)
      else:
        cdi_category = CDICategory.objects.create(name=catID)

      if WordInfo.objects.filter(lemma=item_name).exists():
        word_info = WordInfo.objects.get(lemma=item_name)
      else:
        word_info = WordInfo.objects.create(lemma=item_name, CDI_cat=cdi_category)

      WordMapping.objects.create(word_info=word_info,
                                 instrument=instruments_map,
                                 short_column=item_name,
                                 long_column=item_description)

