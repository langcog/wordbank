from django.db import models


class WordInfo(models.Model):
    uni_lemma = models.CharField(primary_key=True, max_length=20)
    lang_lemma = models.CharField(max_length=20)


class InstrumentsMap(models.Model):
    language = models.CharField(max_length=20)
    forms = (('WS', 'Words & Sentences'), ('WG', 'Words & Gestures'))
    form = models.CharField(max_length=2, choices=forms)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    has_grammar = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=50)
    lexical_category = models.CharField(max_length=20)

class WordMapping(models.Model):
    instrument = models.ForeignKey(InstrumentsMap)
    item = models.CharField(max_length=50)
    item_id = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    category = models.ForeignKey(Category, null=True)
    word_info = models.ForeignKey(WordInfo, null=True, blank=True)
    definition = models.CharField(max_length=200, null=True, blank=True)
    gloss = models.CharField(max_length=80, null=True, blank=True)
    #lexical_category = models.CharField(max_length=30, null=True, blank=True)
    complexity_category = models.CharField(max_length=30, null=True, blank=True)


class MomEd(models.Model):
    level = models.CharField(max_length=20, null=True, blank=True)
    order = models.IntegerField(unique=True)

    class Meta:
        ordering = ["order"]


class Child(models.Model):

    study_id = models.CharField(max_length=20)

    birth_order = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    ethnicities = (('A', 'Asian'), ('B', 'Black'), ('H', 'Hispanic'), ('W', 'White'), ('O', 'Other/Mixed'))
    ethnicity = models.CharField(max_length=1, choices=ethnicities, null=True, blank=True)

    momed = models.ForeignKey(MomEd, null=True, blank=True)
    study_momed = models.CharField(max_length=100, null=True, blank=True)

    sexes = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    sex = models.CharField(max_length=1, choices=sexes, null=True, blank=True)


class Source(models.Model):
    name = models.CharField(max_length=20)
    dataset = models.CharField(max_length=20, null=True, blank=True)
    instrument_language = models.CharField(max_length=20)
    instrument_form = models.CharField(max_length=20)


class Administration(models.Model):
    child = models.ForeignKey(Child)
    instrument = models.ForeignKey(InstrumentsMap)
    source = models.ForeignKey(Source, null=True, blank=True)
    date_of_test = models.DateField(null=True, blank=True)
    data_id = models.IntegerField()
    age = models.IntegerField()
    data_age = models.IntegerField(null=True, blank=True)
    production = models.IntegerField(null=True)
    comprehension = models.IntegerField(null=True)
