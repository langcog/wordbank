from django.core.management.base import BaseCommand
from instruments import aggregate_stats_helper
import json


# Uses aggregate_stats_helper to retrieve each Administration object's data for printing.
# Dumps it to JSON and writes the result to 'static/json/stats.json'.
class Command(BaseCommand):
    def handle(self, *args, **options):
        data = aggregate_stats_helper.aggregate()
        f = open("static/json/stats.json", "w")
        f.write(json.dumps(data, sort_keys=True, indent=4, separators=(",", ": ")))
        f.close()
