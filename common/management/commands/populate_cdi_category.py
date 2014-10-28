from django.core.management.base import NoArgsCommand
from common.models import *

import xlrd

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    book = xlrd.open_workbook(args[0])

    sh = book.sheet_by_index(0)
    nrows = sh.nrows

    for row in range(1, nrows):
      row_values = list(sh.row_values(row))
      word = row_values[0]
      category_name = row_values[1]
      if CDICategory.objects.filter(name=category_name).exists():
        category = CDICategory.objects.get(name=category_name)
      else:
        category = CDICategory.objects.create(name=category_name)
      if not WordInfo.objects.filter(lemma=word).exists():
          WordInfo.objects.create(lemma=word, CDI_cat=category)