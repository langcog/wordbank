# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_administration_norming'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='norming',
        ),
    ]
