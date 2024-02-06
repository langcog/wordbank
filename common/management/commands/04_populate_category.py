import csv
from django.core.management.base import BaseCommand
from common.models import *


# Populates the ItemCategory model with data from 'raw_data/categories.csv'.
class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = list(csv.reader(open("raw_data/categories.csv", "rU")))

        for row in categories:
            name = row[0]
            lexical_category = row[1]
            lexical_class = row[2]
            # for name, lexical_category, lexical_class, complexity_category in categories:
            new_category, created = ItemCategory.objects.get_or_create(
                category=name,
                lexical_category=lexical_category,
                lexical_class=lexical_class,
            )
