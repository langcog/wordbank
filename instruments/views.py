from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import View
from common.models import *

class Search(View):

  def get(self, request):
    return render(request, 'search.html', {})
