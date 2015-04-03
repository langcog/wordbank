# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0023_auto_20150402_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmapping',
            name='item',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
