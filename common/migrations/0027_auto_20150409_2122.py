# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0026_auto_20150409_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmapping',
            name='gloss',
            field=models.CharField(max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
    ]
