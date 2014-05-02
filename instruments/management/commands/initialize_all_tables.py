from django.core.management.base import NoArgsCommand
from common.models import *

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    if len(InstrumentsMap.objects.filter(name='WS', language='english')) <= 0:
      InstrumentsMap.objects.create(name='WS', language='english')
    if len(InstrumentsMap.objects.filter(name='WG', language='english')) <= 0:
      InstrumentsMap.objects.create(name='WG', language='english')
