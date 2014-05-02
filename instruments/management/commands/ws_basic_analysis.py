from django.core.management.base import NoArgsCommand
from common.models import *
from instruments.models import *
import xlrd

class Command(NoArgsCommand):

  def handle(self, *args, **options):
    genders = Child.objects.values('gender').distinct()
    ages = Administration.objects.values('age').distinct()
    gender_values = [d['gender'] for d in genders]
    age_values = [d['age'] for d in ages]
    for g in gender_values:
      for age in age_values:
        objs = WS.objects.filter(child__gender=g, administration__age=age)
        print objs 
