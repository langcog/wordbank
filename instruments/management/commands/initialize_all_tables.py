from django.core.management.base import NoArgsCommand
from common.models import *

class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instruments = open('raw_data/instruments_future.txt', 'r').read().split('\n')
        instruments = filter(lambda i: i != '', instruments)

        for instrument in instruments:

            instrument_language, instrument_name = instrument.split('_')

            if len(InstrumentsMap.objects.filter(name=instrument_name, language=instrument_language)) <= 0:
                InstrumentsMap.objects.create(name=instrument_name, language=instrument_language)