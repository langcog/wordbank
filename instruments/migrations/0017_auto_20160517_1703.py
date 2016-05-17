# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0016_english_british_teds_threes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='english_british_teds_threes',
            name='item_113',
            field=models.CharField(max_length=3, null=True, choices=[('yes', 'yes'), ('no', 'no')]),
        ),
    ]
