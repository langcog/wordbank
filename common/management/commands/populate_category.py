import csv
from django.core.management.base import BaseCommand
from common.models import *


# Populates the Category model with data from 'raw_data/categories.csv'.
class Command(BaseCommand):

    def handle(self, *args, **options):

        categories = list(csv.reader(open('raw_data/categories.csv', 'rU')))

        for name, lexical_category, lexical_class in categories:
            if not Category.objects.filter(name = name,
                                           lexical_category = lexical_category,
                                           lexical_class = lexical_class).exists():
                Category.objects.create(name = name, lexical_category = lexical_category, lexical_class = lexical_class)