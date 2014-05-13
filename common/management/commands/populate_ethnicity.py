from django.core.management.base import NoArgsCommand
from common.models import *

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    ethnicities = {1: "Asian",
                   2: "Black/African American",
                   3: "Hispanic",
                   4: "Other/Mixed"}
    for k in ethnicities:
      Ethnicity.objects.create(id=k, ethnicity=ethnicities[k])

