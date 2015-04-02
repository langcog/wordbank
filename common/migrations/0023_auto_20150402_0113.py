# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0022_auto_20150311_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmapping',
            name='category',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
