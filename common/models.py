from django.db import models

class Child(models.Model):
  study_id = models.CharField(max_length=20)
  gender = models.CharField(max_length=1)
  date_of_birth = models.DateField(null=True, blank=True)
  birth_weight = models.FloatField(null=True, blank=True)
  state = models.CharField(max_length=2, null=True, blank=True)
  gestational_age = models.IntegerField(null=True, blank=True)
  mom_ed = models.IntegerField(null=True, blank=True)
  dad_ed = models.IntegerField(null=True, blank=True)
  birth_order = models.IntegerField(null=True, blank=True)

class InstrumentsMap(models.Model):
  name = models.CharField(max_length=20)
  language = models.CharField(max_length=20)

class Source(models.Model):
  name = models.CharField(max_length=20)
  citation = models.CharField(max_length=20)
  year = models.IntegerField()

class Administration(models.Model):
  child = models.ForeignKey(Child)
  instrument = models.ForeignKey(InstrumentsMap)
  source = models.ForeignKey(Source, null=True, blank=True)
  date_of_test = models.DateField(null=True, blank=True)
  data_id = models.IntegerField()
  age = models.IntegerField()

#Lemma, instrument, short_column, long_column
class WordMapping(models.Model):
  lemma = models.CharField(max_length=20)
  instrument = models.IntegerField()
  short_column = models.CharField(max_length=8)
  long_column = models.CharField(max_length=20)

class WordInfo(models.Model):
  lemma = models.CharField(max_length=20)
  CDI_cat = models.CharField(max_length=20)
