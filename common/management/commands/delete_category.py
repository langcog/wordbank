from django.core.management.base import BaseCommand
from common.models import *


# Deletes all Category objects
class Command(BaseCommand):
    def handle(self, *args, **options):
        ItemCategory.objects.all().delete()
