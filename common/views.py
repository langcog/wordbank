from django.http import HttpResponse
from django.views.generic import View
from common.models import *

class Home(View):

  def get(self, request):
    return HttpResponse('<html>home page</html>')
