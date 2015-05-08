import json
from django.core.management.base import BaseCommand
from common.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        sources = json.load(open('static/json/datasets.json'))

        for source in sources:
            if Source.objects.filter(name=source['name'],
                                     dataset=source['dataset'],
                                     instrument_language=source['instrument_language'],
                                     instrument_form=source['instrument_form']).exists():
                source_obj = Source.objects.get(name=source['name'],
                                                dataset=source['dataset'],
                                                instrument_language=source['instrument_language'],
                                                instrument_form=source['instrument_form'])
                source_obj.contributor = source['contributor']
                source_obj.citation = source['citation']
                source_obj.save()
            else:
                Source.objects.create(name=source['name'],
                                      dataset=source['dataset'],
                                      instrument_language=source['instrument_language'],
                                      instrument_form=source['instrument_form'],
                                      contributor = source['contributor'],
                                      citation = source['citation'])
