# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0019_wordmapping_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='administration',
            name='comprehension',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='administration',
            name='production',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
