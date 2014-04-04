from django.db import models

class Child(models.Model):
  study_id = models.IntegerField()
  dob = models.DateField()
  birth_weight = models.FloatField()
  state = models.CharField(max_length=2)
  gestational_age = models.IntegerField()
  #mom_ed
  #dad_ed
  #birth_order

class InstrumentsMap(models.Model):
  name = models.CharField(max_length=20)
  language = models.CharField(max_length=20)

class Source(models.Model):
  name = models.CharField(max_length=20)
  citation = models.CharField(max_length=20)
  year = models.IntegerField()

