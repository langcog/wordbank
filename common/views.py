from django.http import HttpResponse
from django.db import connection
from django.db import models
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.conf import settings

from common.models import *
from wordbank import settings
import shutil
import csv
import os

class Home(View):

  def get(self, request):
    return render(request, 'home.html', {})


class About(View):

  def get(self, request):
    return render(request, 'about.html', {})


class Contribute(View):

  def get(self, request):
    return render(request, 'contribute.html', {})

class Reports(View):
  def get(self, request):
    id = 'wordle_app'
    if 'id' in request.GET:
      id = request.GET['id']
    return render(request, 'reports.html', {
      'shinyServerIP': settings.SHINY_SERVER_IP, 
      'id': id})

class Survey(View):
  def get(self, request):
    word = request.GET['word']
    df = read_csv(os.path.join(settings.MEDIA_ROOT,'semdata.csv'))
    featuredicts = []
    for row in df.iterrows():
      if row[1]['word'] == word:
        newdict = {}
        newdict[row[1]['feature']] = row[1]['frequency']
        featuredicts.append(newdict)
    return render(request, 'survey.html', {'word': word, 'semdata': featuredicts})


class Search(View):

  def get(self, request):
    source_names = [d.name for d in Source.objects.all()]
    return render(request, 'search.html', {'source_names': source_names})

