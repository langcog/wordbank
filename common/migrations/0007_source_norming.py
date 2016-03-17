# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20151021_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='norming',
            field=models.BooleanField(default=False),
        ),
    ]
