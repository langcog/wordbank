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


class Search(View):
  
  def get(self, request):
    if 'instrument' in request.GET:
      all_admin = Administration.objects.all()
      if 'dob1' in request.GET:
      	print "HELLO"
        #all_admin = all_admin.filter(child__date_of_birth__gte=request.GET.get('dob1'))
        #all_admin = all_admin.filter(child__date_of_birth__lte=request.GET.get('dob2'))
        #print request.GET.get['dob1']
      if 'source_name' in request.GET:
        all_admin = all_admin.filter(source__name=request.GET.get('source_name'))
      if 'source_year' in request.GET:
        all_admin = all_admin.filter(child__date_of_birth__gte=request.GET.get('source_year1'))
        all_admin = all_admin.filter(source__year__lte=request.GET.get('source_year2'))
      #if 'gender' in request.GET:
        #all_admin.filter(gender = request.GET['gender'])
      if 'gestational_age' in request.GET:
        all_admin = all_admin.filter(child__gestational_age__gte=int(request.GET.get('gest_age1')))
        all_admin = all_admin.filter(child__gestational_age__lte=int(request.GET.get('gest_age2')))
      if 'mom_ed' in request.GET:
        all_admin = all_admin.filter(child__mom_ed__gte=int(request.GET.get('mom_ed1')))
        all_admin = all_admin.filter(child__mom_ed__lte=int(request.GET.get('mom_ed2')))
      if 'birth_order' in request.GET:
        all_admin = all_admin.filter(child__birth_order=int(request.GET.get('birth_order')))
      if 'instrument' in request.GET:
        all_admin = all_admin.filter(instrument__name=request.GET.get('instrument')) 
      data_dict = helper.aggregate(all_admin)
      return render(request, 'search.html', {'data_dict': data_dict})
    return render(request, 'search.html', {})

  def dump(qs, path):
    model = qs.model
    writer = csv.writer(open(path, 'w'))
    headers = []
    for field in model._meta.fields:
      headers.append(field.name)
    writer.writerow(headers)
	
    for obj in qs:
      row = []
      for field in headers:
        val = getattr(obj, field)
        if callable(val):
          val = val()
        if type(val) == unicode:
          val = val.encode("utf-8")
        row.append(val)
      writer.writerow(row)

