from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class Source(models.Model):
    name = models.CharField(max_length=20)
    dataset = models.CharField(max_length=20, null=True, blank=True)
    instrument_language = models.CharField(max_length=30)
    instrument_form = models.CharField(max_length=20)
    contributor = models.TextField(blank=True)
    citation = models.TextField(blank=True)
    longitudinal = models.BooleanField(default=False)
    licenses = (('CC-BY', 'CC BY 4.0'),
                ('CC-BY-NC', 'CC BY-NC 4.0'))
    license = models.CharField(max_length=15, choices=licenses)


class Instrument(models.Model):
    language = models.CharField(max_length=30)
    forms = (('WS', 'Words & Sentences'), ('WG', 'Words & Gestures'),
             ('TC', 'Toddler Checklist'), ('IC', 'Infant Checklist'),
             ('TEDS Twos', 'TEDS Twos'), ('TEDS Threes', 'TEDS Threes'),
             ('FormA', 'FormA'), ('FormBOne', 'FormBOne'),
             ('FormBTwo', 'FormBTwo'), ('FormC', 'FormC'))
    form = models.CharField(max_length=12, choices=forms)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    has_grammar = models.BooleanField(default=False)
    unilemma_coverage = models.DecimalField(null=True, max_digits=3, decimal_places=2)

    def __str__(self):
        return f'{self.language} {self.form}'

class Category(models.Model):
    name = models.CharField(max_length=50)
    lexical_category = models.CharField(max_length=20)
    lexical_class = models.CharField(max_length=20)


class ItemMap(models.Model):
    uni_lemma = models.CharField(primary_key=True, max_length=50)


class ItemInfo(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    item_id = models.CharField(max_length=20, db_index=True)
    type = models.CharField(max_length=30)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    map = models.ForeignKey(ItemMap, null=True, blank=True, on_delete=models.SET_NULL)
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

    momed = models.ForeignKey(MomEd, null=True, blank=True, on_delete=models.SET_NULL)
    study_momed = models.CharField(max_length=100, null=True, blank=True)

    sexes = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    sex = models.CharField(max_length=1, choices=sexes, null=True, blank=True)

    zygosities = (('M', 'Monozygotic'), ('D', 'Dizygotic'))
    zygosity = models.CharField(max_length=2, choices=zygosities, null=True, blank=True)

    study_family_id = models.CharField(max_length=20, null=True)

    conditions = models.ManyToManyField('Condition')
    born_early_or_late = models.CharField(max_length = 5, choices = (('early', 'early'),('late', 'late')), blank=True, null=True) # Determines if child was born earlier or later than due date
    birth_weight = models.FloatField(blank=True, null=True) # Declared birthweight in kg (load program must apply calc)
    gestational_age = models.IntegerField(blank=True, null=True, 
        validators=[
            MinValueValidator(25),
            MaxValueValidator(50)
        ] )

    def __str__(self):
        return f'{self.study_id} {self.date_of_birth}'
    
    


class Administration(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, null=True, blank=True, on_delete=models.SET_NULL)
    norming = models.BooleanField(default=False)
    date_of_test = models.DateField(null=True, blank=True)
    data_id = models.IntegerField(db_index=True)
    age = models.IntegerField()
    data_age = models.IntegerField(null=True, blank=True)
    production = models.IntegerField(null=True)
    comprehension = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.instrument} {self.child}'

class CategorySize(models.Model):
    data_id = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    production = models.IntegerField(null=True)
    comprehension = models.IntegerField(null=True)

class Condition(models.Model):
    name = models.CharField(max_length=51, unique=True)

    def __str__(self):
        return f'{self.name}'

class LanguageExposure(models.Model):
    administration = models.ForeignKey(Administration, on_delete=models.CASCADE)
    language = models.CharField(max_length=51)
    language_from = models.CharField(max_length = 50, blank = True, null=True) # Free text response that asks who child hears other languages from
    language_days_per_week = models.IntegerField(null=True, blank = True, validators = [MaxValueValidator(7), MinValueValidator(1)], ) # Asks to quantify the # of days in a week that child is exposed to another language
    language_hours_per_day = models.IntegerField(null=True, blank = True, validators = [MaxValueValidator(24), MinValueValidator(1)],) # Asks to quantify the # of hours a day that child is exposed to another language
    proportion = models.IntegerField(blank=True, null=True,  #proportion of time on language for this administration
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ] )
    age_of_acquisition = models.IntegerField(blank=True, null=True,  #age in months of language acquisition
        validators=[
            MinValueValidator(0)
        ] )

    def __str__(self):
        return f'{self.administration} {self.language}'

    class Meta:
        ordering = ['administration']