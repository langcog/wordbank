from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import View
from common.models import *
from instruments.models import *


class Stats(View):

  def get(self, request):
    #for field in WS._meta.fields:
    
    return render(request, 'stats.html', {})


class Search(View):

  def get(self, request):
    return render(request, 'search.html', {})
