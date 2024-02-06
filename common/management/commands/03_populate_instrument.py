import json, os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.templatetags.static import static

from common.models import *

FORM_DICT = {
    "WS": "WS",
    "WG": "WG",
    "WGComp": "WG",
    "WGShort": "WG",
    "WGShortProd": "WG",
    "WGProdShort": "WG",
    "WGProd": "WG",
    "IC": "WG",
    "TC": "WS",
    "TEDS Twos": "WS",
    "TEDS Threes": "WS",
    "FormA": "WG",
    "FormBOne": "WS",
    "FormBTwo": "WS",
    "FormC": "WS",
    "Oxford CDI": "WG",
    "Swingley": "WG",
    "FormOne": "WG",
    "FormTwoA": "WG",
    "FormTwoB": "WG",
    "FormThree": "WS",
    "CDITwo": "WG",
    "WSShort": "WS",
    "WGShort": "WG",
    "OxfordShort": "WG",
    "WSOther": "WS",
}


# Populates the Instrument model with all instruments in 'static/json/instruments.json'.
# If any instruments already exist (identified by language and form, updates their other fields.
class Command(BaseCommand):
    def handle(self, *args, **options):
        instruments = json.load(open("static/json/instruments.json", encoding="utf8"))

        for instrument in instruments:
            instrument_language, instrument_form = (
                instrument["language"],
                instrument["form"],
            )
            instrument_age_min, instrument_age_max = (
                instrument["age_min"],
                instrument["age_max"],
            )
            instrument_has_grammar = instrument["has_grammar"]
            # instrument_unilemma_coverage = instrument['unilemma_coverage']

            instrument_form_type = FORM_DICT[instrument_form]
            data_dict = {
                "age_min": instrument_age_min,
                "age_max": instrument_age_max,
                "has_grammar": instrument_has_grammar,
                "form_type": instrument_form_type
                #'unilemma_coverage': instrument_unilemma_coverage
            }

            instrument, created = Instrument.objects.update_or_create(
                language=instrument_language, form=instrument_form, defaults=data_dict
            )
