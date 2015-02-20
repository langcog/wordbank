# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0018_delete_ethnicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordmapping',
            name='item_id',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
