from django.core.management.base import BaseCommand
from common.models import *
import instruments.models
from collections import defaultdict


# Populates the CategorySize objects with each data_id entry's Administration object and number of words
# produced/comprehended in each Category by that object's data_id entry in the corresponding instruments model.
# Given no arguments, does so for all instruments in 'static/json/instruments.json'.
# Given a language with -l and a form with -f, does so for only their Instrument object.
class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        CategorySize.objects.all().delete()
        Instrument.objects.all().delete()
        ItemInfo.objects.all().delete()
        ItemMap.objects.all().delete()
        MomEd.objects.all().delete()
        Source.objects.all().delete()
        Administration.objects.all().delete()