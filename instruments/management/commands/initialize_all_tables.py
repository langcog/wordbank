import json
from django.core.management.base import NoArgsCommand
from common.models import *

class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instruments = json.load(open('static/json/instruments.json'))

        for instrument in instruments:

            instrument_language, instrument_form = instrument['language'], instrument['form']

            if len(InstrumentsMap.objects.filter(language=instrument_language, form=instrument_form)) <= 0:
                InstrumentsMap.objects.create(language=instrument_language, form=instrument_form)