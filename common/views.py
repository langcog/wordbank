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
    language_sources_dict = defaultdict(lambda: defaultdict(list))
    for source in sources:
#      language_sources_dict[source.instrument_language].append(source)
      language_sources_dict[source.instrument_language][(source.contributor, source.instrument_form, source.citation)].append(source.n)
#    languages = sorted(language_sources_dict.keys(), key = lambda lang: len(language_sources_dict[lang]), reverse = True)

    languages = sorted(language_sources_dict.keys())
    language_sources_list = [[language, dict(language_sources_dict[language])] for language in languages]
#    print language_sources_list

    num_cols = 2
    col_size = (sum([sum([len(sources) for contributor, sources in language_sources.iteritems()]) for language, language_sources in language_sources_list]) + len(language_sources_list)*2) / num_cols
#    print col_size

    columns = {}
    col_index = 1
    item_buffer = []
    buffer_size = 0
    for language, language_sources in language_sources_list:
      item_buffer.append([language, language_sources])
      buffer_size += len(language_sources) + 2
      if buffer_size >= col_size:
        columns[col_index] = item_buffer
        col_index += 1
        item_buffer = []
        buffer_size = 0
      columns[col_index] = item_buffer
#    print columns

    return render(request, 'contributors.html', {'columns': columns})

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
