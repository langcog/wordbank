from django.http import HttpResponse
from django.db import connection
from django.db import models
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.conf import settings
from common.models import *
from instruments.models import *
from instruments.helper import *
from pandas import*
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
    return render(request, 'reports.html', {'id': id]})

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
    if request.method == 'GET' and 'instrument' in request.GET:
      instrument = (request.GET['instrument'])
      #if instrument == 'WS':
        #sql_string = "SELECT * FROM common_administration JOIN instruments_ws ON common_administration.data_id = instruments_ws.basetable_ptr_id JOIN common_child ON common_administration.child_id = common_child.id WHERE"
      #if instrument == 'WG':
        #sql_string = "SELECT * FROM common_administration JOIN instruments_wg ON common_administration.data_id = instruments_wg.basetable_ptr_id JOIN common_child ON common_administration.child_id = common_child.id WHERE"
      
      all_admin = Administration.objects.filter(instrument__name=((request.GET['instrument'])))
      #if 'dob1' in request.GET:
        #all_admin = all_admin.filter(Child__date_of_birth__gte=(request.GET['dob1']))
        #all_admin = all_admin.filter(Child__date_of_birth__lte=(request.GET['dob2']))
      if 'source_name' in request.GET:
        q = (request.GET['source_name'])
        if q is not None and q != '':
          all_admin = all_admin.filter(Source__name=(request.GET['source_name']))
      if 'source_year' in request.GET:
        q = (request.GET['source_year1'])
        if q is not None and q != '':
          all_admin = all_admin.filter(Source__year__gte=(request.GET['source_year1']))
          all_admin = all_admin.filter(Source__year__lte=(request.GET['source_year2']))
      #if 'gender' in request.GET:
        #all_admin.filter(gender = request.GET['gender'])
      # if 'gestational_age' in request.GET:
      #   q = (request.GET['gest_age1'])
      #   if q is not None and q != '':
           #all_admin = all_admin.filter(Child__gestational_age__gte=int((request.GET['gest_age1'])))
           #all_admin = all_admin.filter(Child__gestational_age__lte=int((request.GET['gest_age2'])))
      if 'mom_ed' in request.GET:
        q = (request.GET['mom_ed1'])
        if q is not None and q != '':
          all_admin = all_admin.filter(child__mom_ed__gte=int((request.GET['mom_ed1'])))
          all_admin = all_admin.filter(child__mom_ed__lte=int((request.GET['mom_ed2'])))
      if 'birth_order' in request.GET:
        q = ((request.GET['birth_order']))
        if q is not None and q != '':
          all_admin = all_admin.filter(child__birth_order=int((request.GET['birth_order'])))
          #newstring = " common_child.birth_order=" + str(q)
          #sql_string =  sql_string + newstring
      for subclass in BaseTable.__subclasses__():
        if instrument == subclass.__name__:
          instrument_class = subclass
          break
      idlist = []
      cursor = connection.cursor()
      #cursor.execute(sql_string)
      #desc = cursor.description
      #data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
      for adm in all_admin.iterator():
        idlist.append(adm.data_id)
      data_dict = []
      for elem in idlist:
        new_dict = {}
        cur_child = Child.objects.filter(administration__data_id=elem).values()[0]
        cur_source = Source.objects.filter(administration__data_id=elem).values()[0]
        cur_obj = instrument_class.objects.filter(pk=elem).values()[0]
        final_dict = dict(cur_child.items() + cur_source.items() + cur_obj.items())
        data_dict.append(final_dict)
      #data_dict = instrument_class.objects.filter(pk__in= idlist).values()
      keys = data_dict[0].keys()
      f = open(os.path.join(settings.MEDIA_ROOT,'file.csv'), 'wb')
      #f = open('/tmp/data.csv','wb')
      dict_writer = csv.DictWriter(f,keys)
      dict_writer.writer.writerow(keys)
      dict_writer.writerows(data_dict)
      f.close()
      #data_dict = aggregate(all_admin)
      #instrument = request.GET['instrument']
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
      return render(request, 'search.html', {'data': '/tmp/data.csv'})
    return render(request, 'search.html', {})
