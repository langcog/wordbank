from django.core.management.base import NoArgsCommand
from instruments import helper
import json

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    data = helper.aggregate()  
    f = open('static/json/stats.json', 'w')
    f.write(json.dumps(data))    
    f.close()
