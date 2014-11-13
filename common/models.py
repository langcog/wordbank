from django.db import models


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=30)


class WordInfo(models.Model):
    uni_lemma = models.CharField(primary_key=True, max_length=20)
    lang_lemma = models.CharField(max_length=20)


class InstrumentsMap(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)


class WordMapping(models.Model):
    column = models.CharField(max_length=8)
    instrument = models.ForeignKey(InstrumentsMap)
    category = models.CharField(max_length=20, null=True, blank=True)
    definition = models.CharField(max_length=100)
    word_info = models.ForeignKey(WordInfo)


class Child(models.Model):
    study_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    birth_weight = models.FloatField(null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    gestational_age = models.IntegerField(null=True, blank=True)
    mom_ed = models.IntegerField(null=True, blank=True)
    dad_ed = models.IntegerField(null=True, blank=True)
    birth_order = models.IntegerField(null=True, blank=True)
    ethnicity = models.ForeignKey(Ethnicity, null=True, blank=True)


class Source(models.Model):
    name = models.CharField(max_length=20)
    dataset = models.CharField(max_length=20, null=True, blank=True)
    instrument = models.CharField(max_length=20, null=True, blank=True)
    citation = models.CharField(max_length=50)


class Administration(models.Model):
    child = models.ForeignKey(Child)
    instrument = models.ForeignKey(InstrumentsMap)
    source = models.ForeignKey(Source, null=True, blank=True)
    date_of_test = models.DateField(null=True, blank=True)
    data_id = models.IntegerField()
    age = models.IntegerField(null=True, blank=True)
    data_age = models.IntegerField(null=True, blank=True)


