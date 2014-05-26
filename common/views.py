from django.http import HttpResponse
from django.db import connection
from django.db import models
from django.shortcuts import render, render_to_response
from django.views.generic import View
from common.models import *
from instruments.helper import *
import csv

class Home(View):

  def get(self, request):
    return render(request, 'home.html', {})


class About(View):

  def get(self, request):
    return render(request, 'about.html', {})


class Contribute(View):

  def get(self, request):
    return render(request, 'contribute.html', {})

class Search(View):

  def search(request):
    if request.GET:
      all_admin = Administrator.objects.all()
      if 'dob1' in request.GET:
        all_admin = all_admin.filter(Child__date_of_birth__gte=request.GET['dob1'])
        all_admin = all_admin.filter(Child__date_of_birth__lte=request.GET['dob2'])
      if 'source_name' in request.GET:
        all_admin = all_admin.filter(Source__name=request.GET['source_name'])
      if 'source_year' in request.GET:
        all_admin = all_admin.filter(Child__date_of_birth__gte=request.GET['source_year1'])
        all_admin = all_admin.filter(Source__year__lte=request.GET['source_year2'])
      #if 'gender' in request.GET:
        #all_admin.filter(gender = request.GET['gender'])
      if 'gestational_age' in request.GET:
        all_admin = all_admin.filter(Child__gestational_age__gte=int(request.GET['gest_age1']))
        all_admin = all_admin.filter(Child__gestational_age__lte=int(request.GET['gest_age2']))
      if 'mom_ed' in request.GET:
        all_admin = all_admin.filter(Child__mom_ed__gte=int(request.GET['mom_ed1']))
        all_admin = all_admin.filter(Child__mom_ed__lte=int(request.GET['mom_ed2']))
      if 'birth_order' in request.GET:
        all_admin = all_admin.filter(Child__birth_order=int(request.GET['birth_order']))
      if 'instrument' in request.GET:
        all_admin = all_admin.filter(InstrumentsMap__name=request.GET['instrument'])
      data = aggregate(all_admin)
      return render(request, 'search.html', {})
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

