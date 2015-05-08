from django.core.management.base import NoArgsCommand
from common.models import *


class Command(NoArgsCommand):

    def handle(self, *args, **options):

        ItemInfo.objects.all().delete()
        ItemMap.objects.all().delete()