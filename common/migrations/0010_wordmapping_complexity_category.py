# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20150111_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordmapping',
            name='complexity_category',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
