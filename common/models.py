from django.db import models

class Child(models.Model):
  study_id = models.IntegerField()
  gender = models.CharField(max_length=)
  date_of_birth = models.DateField()
  birth_weight = models.FloatField()
  state = models.CharField(max_length=2)
  gestational_age = models.IntegerField()
  mom_ed = models.IntegerField()
  dad_ed = models.IntegerField()
  birth_order = models.IntegerField()

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
  source = models.ForeignKey(Source)
  date_of_test = models.DateField()
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
