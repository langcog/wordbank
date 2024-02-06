from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

# Register your models here.

from common.models import *

admin.site.register(LanguageExposure)


class DatasetAdmin(admin.ModelAdmin):
    search_fields = ['dataset_name']
    list_filter = ['dataset_name']
admin.site.register(Dataset, DatasetAdmin)


class ChildAdmin(admin.ModelAdmin):
    search_fields = ["study_internal_id"]
    list_filter = [("dataset_origin", RelatedDropdownFilter)]


admin.site.register(Child, ChildAdmin)


class AdministrationAdmin(admin.ModelAdmin):
    search_fields = ["child__study_internal_id"]
    list_filter = [("dataset", RelatedDropdownFilter)]


admin.site.register(Administration, AdministrationAdmin)
