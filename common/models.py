import json
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.forms.models import model_to_dict
from django.core.validators import MaxValueValidator, MinValueValidator


class DatasetOrigin(models.Model):
    dataset_origin_name = models.CharField(max_length=251, primary_key=True)

    def __str__(self):
        return f"{self.dataset_origin_name}"

    class Meta:
        db_table = "common_dataset_origin"


class Dataset(models.Model):
    dataset_name = models.CharField(max_length=121)
    source = models.CharField(max_length=121, blank=True, null=True)
    contributor = models.TextField(blank=True)
    citation = models.TextField(blank=True)
    licenses = (("CC-BY", "CC BY 4.0"), ("CC-BY-NC", "CC BY-NC 4.0"))
    license = models.CharField(max_length=15, choices=licenses)

    instrument = models.ForeignKey("Instrument", on_delete=models.CASCADE)
    dataset_origin = models.ForeignKey(DatasetOrigin, on_delete=models.CASCADE)
    file_location = models.CharField(max_length=255, blank=True, null=True)
    splitcol = models.CharField(max_length=21, blank=True, null=True)
    norming = models.CharField(max_length=21, blank=True, null=True)
    date_format = models.CharField(max_length=21, blank=True, null=True)

    longitudinal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.dataset_name} ({self.dataset_origin}): {self.instrument}"

    class Meta:
        ordering = ['dataset_name']

class Instrument(models.Model):
    language = models.CharField(max_length=30)
    forms = (
        ("WS", "Words & Sentences"),
        ("WG", "Words & Gestures"),
        ("TC", "Toddler Checklist"),
        ("IC", "Infant Checklist"),
        ("TEDS Twos", "TEDS Twos"),
        ("TEDS Threes", "TEDS Threes"),
        ("FormA", "FormA"),
        ("FormBOne", "FormBOne"),
        ("FormBTwo", "FormBTwo"),
        ("FormC", "FormC"),
    )
    form = models.CharField(max_length=12, choices=forms)
    form_type = models.CharField(max_length=12)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    has_grammar = models.BooleanField(default=False)
    unilemma_coverage = models.DecimalField(null=True, max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.language} {self.form}"


class ItemCategory(models.Model):
    category = models.CharField(max_length=50)
    lexical_category = models.CharField(max_length=20)
    lexical_class = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        db_table = "common_item_category"


class UniLemma(models.Model):
    uni_lemma = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = "common_uni_lemma"

    def __str__(self):
        return f"{self.uni_lemma}"


class Item(models.Model):
    item_id = models.CharField(max_length=20, db_index=True)
    item_kind = models.CharField(max_length=30)
    item_definition = models.CharField(max_length=200, null=True, blank=True)
    study_internal_item = models.CharField(max_length=50)
    english_gloss = models.CharField(max_length=80, null=True, blank=True)
    item_category = models.ForeignKey(
        ItemCategory, null=True, on_delete=models.SET_NULL
    )
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    uni_lemma = models.ForeignKey(
        UniLemma, null=True, blank=True, on_delete=models.SET_NULL
    )
    complexity_category = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.item_id} {self.item_definition} {self.english_gloss}"


class CaregiverEducation(models.Model):
    education_level = models.CharField(max_length=20, null=True, blank=True)
    education_order = models.IntegerField(unique=True)

    class Meta:
        ordering = ["education_order"]
        db_table = "common_caregiver_education"

    def __str__(self):
        return f"{self.education_order} {self.education_level}"


class Child(models.Model):
    birth_order = models.IntegerField(null=True, blank=True)

    ethnicities = (
        ("A", "Asian"),
        ("B", "Black"),
        ("H", "Hispanic"),
        ("W", "White"),
        ("O", "Other/Mixed"),
    )
    ethnicity = models.CharField(
        max_length=1, choices=ethnicities, null=True, blank=True
    )

    race = models.CharField(max_length=1, blank=True, null=True)

    sexes = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    sex = models.CharField(max_length=1, choices=sexes, null=True, blank=True)

    zygosities = (("M", "Monozygotic"), ("D", "Dizygotic"))
    zygosity = models.CharField(max_length=2, choices=zygosities, null=True, blank=True)

    born_early_or_late = models.CharField(
        max_length=5,
        choices=(("early", "early"), ("late", "late")),
        blank=True,
        null=True,
    )  # Determines if child was born earlier or later than due date
    birth_weight = models.FloatField(
        blank=True, null=True
    )  # Declared birthweight in kg (load program must apply calc)
    gestational_age = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(25), MaxValueValidator(50)]
    )

    study_internal_id = models.CharField(max_length=201, null=True)
    study_internal_family_id = models.CharField(max_length=20, null=True)

    dataset_origin = models.ForeignKey(
        DatasetOrigin, on_delete=models.CASCADE, null=True
    )

    study_internal_caregiver_education = models.CharField(
        max_length=100, null=True, blank=True
    )
    caregiver_education = models.ForeignKey(
        CaregiverEducation, null=True, blank=True, on_delete=models.SET_NULL
    )

    health_conditions = models.ManyToManyField("HealthCondition")

    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.study_internal_id} {self.dataset_origin}"


class Administration(models.Model):
    is_norming = models.BooleanField(default=False)
    date_of_test = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    study_internal_age = models.IntegerField(null=True, blank=True)
    production = models.IntegerField(null=True)
    comprehension = models.IntegerField(null=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    dataset = models.ForeignKey(
        Dataset, null=True, blank=True, on_delete=models.SET_NULL
    )

    data_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True
    )
    data_id = models.PositiveIntegerField(db_index=True, null=True)
    content_object = GenericForeignKey("data_content_type", "data_id")

    def __str__(self):
        return f"{self.instrument} {self.child}"

    def as_dict(self):
        return model_to_dict(self)


class CategorySize(models.Model):
    data_id = models.IntegerField()
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True)
    production = models.IntegerField(null=True)
    comprehension = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.item_category} {self.data_id}"

    class Meta:
        db_table = "common_category_size"


class HealthCondition(models.Model):
    health_condition_name = models.CharField(max_length=51, unique=True)

    def __str__(self):
        return f"{self.health_condition_name}"

    class Meta:
        db_table = "common_health_condition"


class LanguageExposure(models.Model):
    administration = models.ForeignKey(Administration, on_delete=models.CASCADE)
    language = models.CharField(max_length=51)
    exposure_proportion = models.IntegerField(
        blank=True,
        null=True,  # proportion of time on language for this administration
        validators=[MaxValueValidator(100), MinValueValidator(1)],
    )
    age_of_first_exposure = models.IntegerField(
        blank=True,
        null=True,  # age in months of language acquisition
        validators=[MinValueValidator(0), MaxValueValidator(72)],
    )

    def __str__(self):
        return f"{self.administration} {self.language}"

    class Meta:
        ordering = ["administration"]
        db_table = "common_language_exposure"
