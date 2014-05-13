from django.db import models


class Ethnicity:
  ethnicity = CharField(max_length=30)


class CDICategory(models.Model):
  name = models.CharField(max_length=20)


class WordInfo(models.Model):
  lemma = models.CharField(primary_key=True, max_length=20)
  CDI_cat = models.ForeignKey(CDICategory)


class InstrumentsMap(models.Model):
  name = models.CharField(max_length=20)
  language = models.CharField(max_length=20)


class WordMapping(models.Model):
  word_info = models.ForeignKey(WordInfo)
  instrument = models.ForeignKey(InstrumentsMap)
  short_column = models.CharField(max_length=8)
  long_column = models.CharField(max_length=100)


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
  ethinicity = models.ForeignKey(null=True, blank=True)


class Source(models.Model):
  name = models.CharField(max_length=50)
  citation = models.CharField(max_length=20)


class Administration(models.Model):
  child = models.ForeignKey(Child)
  instrument = models.ForeignKey(InstrumentsMap)
  source = models.ForeignKey(Source, null=True, blank=True)
  date_of_test = models.DateField(null=True, blank=True)
  data_id = models.IntegerField()
  age = models.IntegerField(null=True, blank=True)


