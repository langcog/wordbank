# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20150916_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='data_id',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='iteminfo',
            name='item_id',
            field=models.CharField(max_length=20, db_index=True),
        ),
    ]
