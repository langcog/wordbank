import datetime
import json
import csv

from django.db import connection
from django.db import models

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import View

from common.models import *
from instruments.models import *
from instruments import helper


class Stats(View):

  def get(self, request):
    return render(request, 'stats.html', {'data': []})
