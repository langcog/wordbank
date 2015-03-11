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
