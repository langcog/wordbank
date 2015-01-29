from django.db import models


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=30)


class WordInfo(models.Model):
    uni_lemma = models.CharField(primary_key=True, max_length=20)
    lang_lemma = models.CharField(max_length=20)


class InstrumentsMap(models.Model):
    language = models.CharField(max_length=20)
    form = models.CharField(max_length=20)


class WordMapping(models.Model):
    instrument = models.ForeignKey(InstrumentsMap)
    item = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    word_info = models.ForeignKey(WordInfo, null=True, blank=True)
    definition = models.CharField(max_length=200, null=True, blank=True)
    lexical_category = models.CharField(max_length=30, null=True, blank=True)
    complexity_category = models.CharField(max_length=30, null=True, blank=True)


class Child(models.Model):

    birth_order = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    ethnicities = (('A', 'Asian'), ('B', 'Black'), ('H', 'Hispanic'), ('W', 'White'), ('O', 'Other/Mixed'))
    ethnicity = models.CharField(max_length=1, choices=ethnicities, null=True, blank=True)

    ed_levels = (('nothing', 'nothing'),
                 ('primary', 'primary'),
                 ('some secondary', 'some secondary'),
                 ('secondary', 'secondary'),
                 ('some college', 'some college'),
                 ('college', 'college'),
                 ('some graduate', 'some graduate'),
                 ('graduate', 'graduate'))
    mom_ed = models.CharField(max_length=20, choices=ed_levels, null=True, blank=True)

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


