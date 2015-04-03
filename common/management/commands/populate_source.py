import json
from django.core.management.base import NoArgsCommand
from common.models import *


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        sources = json.load(open('static/json/datasets.json'))

        for source in sources:
            if not Source.objects.filter(name=source['name'],
                                         dataset=source['dataset'],
                                         instrument_language=source['instrument_language'],
                                         instrument_form=source['instrument_form']).exists():
                Source.objects.create(name=source['name'],
                                      dataset=source['dataset'],
                                      instrument_language=source['instrument_language'],
                                      instrument_form=source['instrument_form'])