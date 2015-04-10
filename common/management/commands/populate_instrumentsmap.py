import json
from django.core.management.base import NoArgsCommand
from common.models import *

class Command(NoArgsCommand):

    def handle(self, *args, **options):

        instruments = json.load(open('static/json/instruments.json'))

        for instrument in instruments:

            instrument_language, instrument_form = instrument['language'], instrument['form']
            instrument_age_min, instrument_age_max = instrument['age_min'], instrument['age_max']
            instrument_has_grammar = instrument['has_grammar']

            if not InstrumentsMap.objects.filter(language=instrument_language, form=instrument_form).exists():
                InstrumentsMap.objects.create(language=instrument_language, form=instrument_form,
                                              age_min=instrument_age_min, age_max=instrument_age_max,
                                              has_grammar=instrument_has_grammar)