import json
from django.core.management.base import BaseCommand
from common.models import *


# Populates the Source model with all sources in 'static/json/datasets.json'.
# If any sources already exist (identified by name, dataset, language, and form), updates their other fields.
class Command(BaseCommand):

    def handle(self, *args, **options):

        sources = json.load(open('static/json/datasets.json'))

        for source in sources:

            data_dict = {'contributor': source['contributor'],
                         'citation': source['citation'],
                         'longitudinal': source['longitudinal'],
                         'license': source['license']
            }

            data_set, created = Source.objects.update_or_create(
                                     name=source['name'],
                                     dataset=source['dataset'],
                                     instrument_language=source['instrument_language'],
                                     instrument_form=source['instrument_form'],
                                     defaults=data_dict
                                     )

