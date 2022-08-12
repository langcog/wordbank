import json, os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.templatetags.static import static

from common.models import *


# Populates the Source model with all sources in 'static/json/datasets.json'.
# If any sources already exist (identified by name, dataset, language, and form), updates their other fields.
class Command(BaseCommand):

    def handle(self, *args, **options):

        sources = json.load(open('static/json/datasets.json', encoding="utf8"))
        for source in sources:
            print(f"Loading dataset file {source['file']}")
            
            if 'dataset_origin' in source:
                name = source['dataset_origin']
            else:
                name = source['name']+'_'+source['dataset']+'_'+source['instrument_language']+'_'+source['instrument_form']

            dataset_origin, created = DatasetOrigin.objects.get_or_create(dataset_origin_name=name)

            data_dict = {'contributor': source['contributor'],
                         'citation': source['citation'],
                         'longitudinal': source['longitudinal'],
                         'license': source['license'],
            }

            instrument = Instrument.objects.get(language=source['instrument_language'], form=source['instrument_form'])
            data_set, created = Dataset.objects.update_or_create(
                dataset_origin=dataset_origin,
                dataset_name=source['name'],
                #source_dataset=source['dataset'],
                instrument=instrument,
                defaults=data_dict
                )

