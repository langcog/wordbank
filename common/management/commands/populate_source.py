import json
from django.core.management.base import BaseCommand
from common.models import *


# Populates the Source model with all sources in 'static/json/datasets.json'.
# If any sources already exist (identified by name, dataset, language, and form), updates their other fields.
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
                source_obj.longitudinal = source['longitudinal']
                source_obj.save()
            else:
                Source.objects.create(name=source['name'],
                                      dataset=source['dataset'],
                                      instrument_language=source['instrument_language'],
                                      instrument_form=source['instrument_form'],
                                      contributor = source['contributor'],
                                      citation = source['citation'],
                                      longitudinal = source['longitudinal'])
