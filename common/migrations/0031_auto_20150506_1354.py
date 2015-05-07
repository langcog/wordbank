# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0030_auto_20150423_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentsmap',
            name='language',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
