from django.core.management.base import NoArgsCommand
from common.models import *


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        sources = [{'name': 'Marchman', 'dataset': 'Norming', 'instrument': 'English_WS', 'citation': 'Fenson 2007'},
                   {'name': 'Marchman', 'dataset': 'Wisconsin', 'instrument': 'English_WS', 'citation': 'Marchman'},
                   {'name': 'Marchman', 'dataset': 'Dallas', 'instrument': 'English_WS', 'citation': 'Marchman'},
                   {'name': 'Smith', 'dataset': 'electronic', 'instrument': 'English_WS', 'citation': 'Smith'},
                   {'name': 'Smith', 'dataset': 'paper', 'instrument': 'English_WS', 'citation': 'Smith'},
                   {'name': 'Marchman', 'dataset': 'Norming', 'instrument': 'English_WG', 'citation': ''},
                   {'name': 'Bleses', 'dataset': '', 'instrument': 'Danish_WS', 'citation': 'Bleses'},
                   {'name': 'Kristoffersen', 'dataset': '', 'instrument': 'Norwegian_WS', 'citation': ''},
                   {'name': 'Kristoffersen', 'dataset': 'longitudinal', 'instrument': 'Norwegian_WS', 'citation': ''},
                   {'name': 'Kristoffersen', 'dataset': '', 'instrument': 'Norwegian_WG', 'citation': ''},
                   {'name': 'Kristoffersen', 'dataset': 'longitudinal', 'instrument': 'Norwegian_WG', 'citation': ''}]

        for k in sources:
            Source.objects.create(name=k['name'],
                                  dataset=k['dataset'],
                                  instrument=k['instrument'],
                                  citation=k['citation'])