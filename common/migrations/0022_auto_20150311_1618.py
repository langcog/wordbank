# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_auto_20150304_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumentsmap',
            name='age_max',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrumentsmap',
            name='age_min',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
    ]
