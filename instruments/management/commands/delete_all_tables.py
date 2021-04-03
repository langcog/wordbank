import json
from django.core.management.base import BaseCommand
from common.models import *
import instruments.models
from instruments.utils import get_instrument_model


class Command(BaseCommand):

    def handle(self, *args, **options):

        insts = json.load(open('static/json/instruments.json'))

        for instrument in insts:
            instrument_model = get_instrument_model(instrument['language'], instrument['form'])
            instrument_model.objects.all().delete()

        Instrument.objects.all().delete()
        Category.objects.all().delete()
        ItemInfo.objects.all().delete()
        ItemMap.objects.all().delete()
        MomEd.objects.all().delete()
        Source.objects.all().delete()
        Child.objects.all().delete()
        Administration.objects.all().delete()
