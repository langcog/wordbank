from django.core.management.base import NoArgsCommand
from common.models import *
from instruments.models import *

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    WS.objects.all().delete()
    WG.objects.all().delete()
    Child.objects.all().delete()
    Administration.objects.all().delete()
    InstrumentsMap.objects.all().delete()
    Source.objects.all().delete()
    WordMapping.objects.all().delete()
    WordInfo.objects.all().delete()
    Ethnicity.objects.all().delete()
