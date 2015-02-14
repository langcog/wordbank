# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_auto_20150213_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='momed',
            options={'ordering': ['order']},
        ),
    ]
