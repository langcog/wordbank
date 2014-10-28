from django.core.management.base import NoArgsCommand
from common.models import *

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    sources = {1: {'name': 'Original Norming data', 'citation': 'Fenson'},
               2: {'name': 'San Diego State University', 'citation': 'Thal'},
               3: {'name': 'University of Wisconsin', 'citation': 'Marchman'},
               4: {'name': 'UT Dallas', 'citation': 'Marchman'},
               5: {'name': 'San Diego State University', 'citation': 'Cronan'},
               6: {'name': 'San Diego State University', 'citation': 'Fenson/Newton'},
               7: {'name': 'Louisiana State University', 'citation': 'Oetting'},
               8: {'name': 'University of Connecticut', 'citation': 'Naigles'},
               9: {'name': 'University of California, San Diego', 'citation': 'Trauner'},
               10: {'name': 'Indiana University, Bloomington', 'citation': 'Smith'}}

    for k in sources:
      Source.objects.create(id=k, 
                            name=sources[k]['name'],
                            citation=sources[k]['citation'])

