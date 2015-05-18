import json
from django.core.management.base import BaseCommand
from common.models import *
import instruments.models


class Command(BaseCommand):

    def handle(self, *args, **options):

        insts = json.load(open('static/json/instruments.json'))

        for instrument in insts:
            instrument_model = getattr(instruments.models,
                                       '_'.join(instrument['language'].split() + [instrument['form']]))
            instrument_model.objects.all().delete()

        Instrument.objects.all().delete()
        Category.objects.all().delete()
        ItemInfo.objects.all().delete()
        ItemMap.objects.all().delete()
        MomEd.objects.all().delete()
        Source.objects.all().delete()
        Child.objects.all().delete()
        Administration.objects.all().delete()
