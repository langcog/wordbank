import json
from django.core.management.base import BaseCommand
from common.models import *


# Populates the Instrument model with all instruments in 'static/json/instruments.json'.
# If any instruments already exist (identified by language and form), updates their other fields.
class Command(BaseCommand):

    def handle(self, *args, **options):

        instruments = json.load(open('static/json/instruments.json'))

        for instrument in instruments:

            instrument_language, instrument_form = instrument['language'], instrument['form']
            instrument_age_min, instrument_age_max = instrument['age_min'], instrument['age_max']
            instrument_has_grammar = instrument['has_grammar']

            if Instrument.objects.filter(language=instrument_language, form=instrument_form).exists():
                instrument_obj = Instrument.objects.get(language=instrument_language, form=instrument_form)
                instrument_obj.age_min = instrument_age_min
                instrument_obj.age_max = instrument_age_max
                instrument_obj.has_grammar = instrument_has_grammar
                instrument_obj.save()
            else:
                Instrument.objects.create(language=instrument_language, form=instrument_form,
                                              age_min=instrument_age_min, age_max=instrument_age_max,
                                              has_grammar=instrument_has_grammar)