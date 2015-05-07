# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0031_auto_20150506_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='instrument_language',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
