from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=20)
    dataset = models.CharField(max_length=20, null=True, blank=True)
    instrument_language = models.CharField(max_length=30)
    instrument_form = models.CharField(max_length=20)
    contributor = models.TextField(blank=True)
    citation = models.TextField(blank=True)
    longitudinal = models.BooleanField(default=False)


class Instrument(models.Model):
    language = models.CharField(max_length=30)
    forms = (('WS', 'Words & Sentences'), ('WG', 'Words & Gestures'),
             ('TC', 'Toddler Checklist'), ('IC', 'Infant Checklist'))
    form = models.CharField(max_length=2, choices=forms)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    has_grammar = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=50)
    lexical_category = models.CharField(max_length=20)
    lexical_class = models.CharField(max_length=20)


class ItemMap(models.Model):
    uni_lemma = models.CharField(primary_key=True, max_length=50)


class ItemInfo(models.Model):
    instrument = models.ForeignKey(Instrument)
    item = models.CharField(max_length=50)
    item_id = models.CharField(max_length=20, db_index=True)
    type = models.CharField(max_length=30)
    category = models.ForeignKey(Category, null=True)
    map = models.ForeignKey(ItemMap, null=True, blank=True)
    definition = models.CharField(max_length=200, null=True, blank=True)
    gloss = models.CharField(max_length=80, null=True, blank=True)
    complexity_category = models.CharField(max_length=30, null=True, blank=True)


class MomEd(models.Model):
    level = models.CharField(max_length=20, null=True, blank=True)
    order = models.IntegerField(unique=True)

    class Meta:
        ordering = ["order"]


class Child(models.Model):

    study_id = models.CharField(max_length=20, null=True)

    birth_order = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    ethnicities = (('A', 'Asian'), ('B', 'Black'), ('H', 'Hispanic'), ('W', 'White'), ('O', 'Other/Mixed'))
    ethnicity = models.CharField(max_length=1, choices=ethnicities, null=True, blank=True)

    momed = models.ForeignKey(MomEd, null=True, blank=True)
    study_momed = models.CharField(max_length=100, null=True, blank=True)

    sexes = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    sex = models.CharField(max_length=1, choices=sexes, null=True, blank=True)


class Administration(models.Model):
    child = models.ForeignKey(Child)
    instrument = models.ForeignKey(Instrument)
    source = models.ForeignKey(Source, null=True, blank=True)
    norming = models.BooleanField(default=False)
    date_of_test = models.DateField(null=True, blank=True)
    data_id = models.IntegerField(db_index=True)
    age = models.IntegerField()
    data_age = models.IntegerField(null=True, blank=True)
    production = models.IntegerField(null=True)
    comprehension = models.IntegerField(null=True)


class CategorySize(models.Model):
    data_id = models.IntegerField()
    category = models.ForeignKey(Category)
    production = models.IntegerField(null=True)
    comprehension = models.IntegerField(null=True)
