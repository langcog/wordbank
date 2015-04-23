from django.http import HttpResponse
from django.db import connection
from django.db import models
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.conf import settings
from django.db.models import Count

from common.models import *
from wordbank import settings
import shutil
import csv
import os
from collections import defaultdict

class Home(View):

  def get(self, request):
    return render(request, 'home.html', {})


class About(View):

  def get(self, request):
    return render(request, 'about.html', {})


class Contributors(View):

  def get(self, request):
    sources = Source.objects.annotate(n = Count('administration'))
    language_sources = defaultdict(list)
    for source in sources:
      language_sources[source.instrument_language].append(source)
    languages = sorted(language_sources.keys(), key = lambda lang: len(language_sources[lang]), reverse = True)
    language_sources_list = []
    for language in languages:
      language_sources_list.append([language, language_sources[language]])
    print language_sources_list

    return render(request, 'contributors.html', {'language_sources_list': language_sources_list})

class Reports(View):

  def get(self, request):
    id = None
    if 'id' in request.GET:
      id = request.GET['id']
      return render(request, 'reports.html', {
             'shinyServerIP': settings.SHINY_SERVER_IP,
             'id': id})
    else:
        return render(request, 'reports_landing.html', {})

class Blog(View):

  def get(self, request):
    return render(request, 'blog.html', {})

class Tutorial(View):

  def get(self, request):
    return render(request, 'tutorial.html', {})
