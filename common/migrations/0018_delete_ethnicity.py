# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_auto_20150213_1607'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ethnicity',
        ),
    ]
