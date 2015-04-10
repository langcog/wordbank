# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0025_auto_20150409_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmapping',
            name='category',
            field=models.ForeignKey(to='common.Category'),
            preserve_default=True,
        ),
    ]
