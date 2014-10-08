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

class Reports(View):
  def get(self, request):
    id = 'wordle_app'
    if 'id' in request.GET:
      id = request.GET['id']
    return render(request, 'reports.html', {'id': id]})

class Search(View):

  def get(self, request):
    print 'Hello'
    if request.method == 'GET':
      print 'Hello1'
      all_admin = Administrator.objects.all()
      # if 'dob1' in request.GET:
      #   print "HEllo2"
        # all_admin = all_admin.filter(Child__date_of_birth__gte=(request.GET['dob1'])[2:-1])
        # all_admin = all_admin.filter(Child__date_of_birth__lte=(request.GET['dob2'])[2:-1])
        # print request.GET.get['dob1']
      # if 'source_name' in request.GET:
      #   q = (request.GET['source_name'])[2:-1]
      #   if q is not None and q != '':
      #     all_admin = all_admin.filter(Source__name=(request.GET['source_name'])[2:-1])
      # if 'source_year' in request.GET:
      #   q = (request.GET['source_year1'])[2:-1]
      #   if q is not None and q != '':
      #     all_admin = all_admin.filter(Source__year__gte=(request.GET['source_year1'])[2:-1])
      #     all_admin = all_admin.filter(Source__year__lte=(request.GET['source_year2'])[2:-1])
      #if 'gender' in request.GET:
        #all_admin.filter(gender = request.GET['gender'])
      # if 'gestational_age' in request.GET:
      #   q = (request.GET['gest_age1'])[2:-1]
      #   if q is not None and q != '':
      #     int("HELLO")
      #     all_admin = all_admin.filter(Child__gestational_age__gte=int((request.GET['gest_age1'])[2:-1]))
      #     all_admin = all_admin.filter(Child__gestational_age__lte=int((request.GET['gest_age2'])[2:-1]))
      if 'mom_ed' in request.GET:
        q = (request.GET['mom_ed1'])[2:-1]
        if q is not None and q != '':
          all_admin = all_admin.filter(Child__mom_ed__gte=int((request.GET['mom_ed1'])[2:-1]))
          all_admin = all_admin.filter(Child__mom_ed__lte=int((request.GET['mom_ed2'])[2:-1]))
      if 'birth_order' in request.GET:
        q = (request.GET['birth_order'])[2:-1]
        if q is not None and q != '':
          all_admin = all_admin.filter(Child__birth_order=int((request.GET['birth_order'])[2:-1]))
      if 'instrument' in request.GET:
        q = (request.GET['instrument'])[2:-1]
        if q is not None and q != '':
          all_admin = all_admin.filter(InstrumentsMap__name=(request.GET['instrument'])[2:-1]) 
      data_dict = aggregate(all_admin)
      instrument = (request.GET['instrument'])[2:-1]
      for subclass in BaseTable.__subclasses__():
        if instrument == subclass.__name__:
          instrument_class = subclass
          obj['instrument'] = instrument
          break
      # f = open("filename.csv", "w")
      # f.truncate()
      # f.close()
      # f = open("filename.csv", "w")
      # all_items = []
      # for item in all_admin:
      #   instrument_obj = instrument_class.objects.get(pk=administration.data_id).__dict__
      #   all_items.append(instrument_obj)
      # keys = []
      # for field in instrument_class._meta.fields:
      #   field_name = field.get_attname_column()[0]
      #   keys.append(field_name)
      # dict_writer = csv.DictWriter(f, keys)
      # dict_writer.writer.writerow(keys)
      # dict_writer.writerows(all_items)
      return render(request, 'search.html', {'data_dict': data_dict})
    return render(request, 'search.html', {})
