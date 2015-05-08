from django.core.management.base import BaseCommand
from instruments import aggregate_stats_helper
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = aggregate_stats_helper.aggregate()
        f = open('static/json/stats.json', 'w')
        f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
        f.close()
