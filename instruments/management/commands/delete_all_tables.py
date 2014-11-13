from django.core.management.base import NoArgsCommand
from common.models import *
import instruments.models


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        inst = open('raw_data/instruments.txt', 'r').read().split('\n')
        inst = filter(lambda i: i != '', inst)

        for instrument in inst:
            instrument_model = getattr(instruments.models, instrument)
            instrument_model.objects.all().delete()

        Child.objects.all().delete()
        Administration.objects.all().delete()
        InstrumentsMap.objects.all().delete()
        Source.objects.all().delete()
        WordMapping.objects.all().delete()
#        WordInfo.objects.all().delete()
        Ethnicity.objects.all().delete()
