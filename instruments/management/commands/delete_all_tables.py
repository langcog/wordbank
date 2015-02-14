import json
from django.core.management.base import NoArgsCommand
from common.models import *
import instruments.models


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        insts = json.load(open('static/json/instruments.json'))

        for instrument in insts:
            instrument_model = getattr(instruments.models, '_'.join([instrument['language'], instrument['form']]))
            instrument_model.objects.all().delete()

        Child.objects.all().delete()
        Administration.objects.all().delete()
        MomEd.objects.all().delete()
        InstrumentsMap.objects.all().delete()
        Source.objects.all().delete()
        WordMapping.objects.all().delete()
        WordInfo.objects.all().delete()
