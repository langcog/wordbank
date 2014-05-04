from django.http import HttpResponse
from django.db import connection
from django.db import models
from django.shortcuts import render, render_to_response
from django.views.generic import View
from common.models import *
import csv

class Home(View):

  def get(self, request):
    return render(request, 'home.html', {})

class Search(View):

  def search(request):
  	if request.GET:
  	  all_admin = Administrator.objects.all()
  	  if 'source_name' in request.GET:
  	    all_admin = all_admin.filter(Source__name=request.GET['source_name'])
  	  if 'source_year' in request.GET:
  	    all_admin = all_admin.filter(Source__year=int(request.GET['source_year']))
  	  #if 'gender' in request.GET:
  	    #all_admin.filter(gender = request.GET['gender'])
  	  if 'gestational_age' in request.GET:
  	    all_admin = all_admin.filter(Child__gestational_age=int(request.GET['gestational_age']))
  	  if 'mom_ed' in request.GET:
  	    all_admin = all_admin.filter(Child__mom_ed=int(request.GET['mom_ed']))
  	  if 'birth_order' in request.GET:
	      all_admin = all_admin.filter(Child__birth_order=int(request.GET['birth_order']))
  	  if 'instrument' in request.GET:
  	    all_admin = all_admin.filter(InstrumentsMap__name=request.GET['instrument'])
  	  if 'language' in request.GET:
  	    all_admin = all_admin.filter(InstrumentsMap__language=request.GET['language'])
      dump(all_admin.iterator(),'./raw_data/test.csv')
      #cursor = connection.cursor()
      #for instrument in all_admin.values_list('InstrumentsMap__name').distinct:
        #CODE WHERE WE GET ROWS FROM SPECIFIC INSTRUMENT TABLES
  	    #dump(all_admin.iterator(), './raw_data/test.csv')
  	  return render(request, 'search.html', {})
  	else:
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