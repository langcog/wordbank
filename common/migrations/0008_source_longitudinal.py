# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_source_norming'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='longitudinal',
            field=models.BooleanField(default=False),
        ),
    ]
