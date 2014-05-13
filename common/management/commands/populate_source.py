from django.core.management.base import NoArgsCommand
from common.models import *

class Command(NoArgsComman):

  def handle(self, *args, **options):
    sources = {0: {'name': 'Original Norming data', 'citation': 'Fenson'},
               1: {'name': 'San Diego State University', 'citation': 'Thal'},
               2: {'name': 'University of Wisconsin', 'citation': 'Marchman'},
               3: {'name': 'UT Dallas', 'citation': 'Marchman'},
               4: {'name': 'San Diego State University', 'citation': 'Cronan'},
               5: {'name': 'San Diego State University', 'citation': 'Fenson/Newton'},
               6: {'name': 'Louisiana State University', 'citation': 'Oetting'},
               7: {'name': 'University of Connecticut', 'citation': 'Naigles'},
               8: {'name': 'University of California, San Diego', 'citation': 'Trauner'}}

    for k in sources:
      Source.objects.create(id=k, 
                            name=ethnicities[k]['name'],
                            citation=sources[k]['citation'])

