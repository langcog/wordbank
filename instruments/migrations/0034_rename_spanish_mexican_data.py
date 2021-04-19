# -*- coding: utf-8 -*-


from django.db import models, migrations
from common.models import *

def rename_spanish_models(apps, schema_editor):
    Instrument = apps.get_model("common", "Instrument")
    Source = apps.get_model("common", "Source")
    Instrument.objects.filter(language = 'Spanish').update(language = 'Spanish (Mexican)')
    Source.objects.filter(instrument_language = 'Spanish').update(instrument_language = 'Spanish (Mexican)')

def reverse_spanish_models(apps, schema_editor):
    Instrument = apps.get_model("common", "Instrument")
    Source = apps.get_model("common", "Source")
    Instrument.objects.filter(language = 'Spanish (Mexican)').update(language = 'Spanish')
    Source.objects.filter(instrument_language = 'Spanish (Mexican)').update(instrument_language = 'Spanish')


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0033_rename_languages'),
    ]

    operations = [
        migrations.RunPython(rename_spanish_models, reverse_spanish_models),
        migrations.RenameModel(
            old_name='Spanish_WG',
            new_name='Spanish_Mexican_WG',
        ),
        migrations.RenameModel(
            old_name='Spanish_WS',
            new_name='Spanish_Mexican_WS',
        ),
    ]
