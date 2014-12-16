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
    item = models.CharField(max_length=20)
    instrument = models.ForeignKey(InstrumentsMap)
    category = models.CharField(max_length=20, null=True, blank=True)
    definition = models.CharField(max_length=100)
    word_info = models.ForeignKey(WordInfo)


class Child(models.Model):
    birth_order = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    ethnicities = (('A', 'Asian'), ('B', 'Black'), ('H', 'Hispanic'), ('W', 'White'), ('O', 'Other/Mixed'))
    ethnicity = models.CharField(max_length=1, choices=ethnicities, null=True, blank=True)
    mom_ed = models.IntegerField(null=True, blank=True)
    sexes = (('M', 'Male'), ('F', 'Female'))
    sex = models.CharField(max_length=1, choices=sexes, null=True, blank=True)
    study_id = models.CharField(max_length=20)
#    birth_weight = models.FloatField(null=True, blank=True)
#    state = models.CharField(max_length=2, null=True, blank=True)
#    gestational_age = models.IntegerField(null=True, blank=True)
#    dad_ed = models.IntegerField(null=True, blank=True)


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
    age = models.IntegerField()
    data_age = models.IntegerField(null=True, blank=True)


