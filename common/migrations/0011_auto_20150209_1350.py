# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_wordmapping_complexity_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentsmap',
            name='form',
            field=models.CharField(max_length=2, choices=[(b'WS', b'Words & Sentences'), (b'WG', b'Words & Gestures')]),
            preserve_default=True,
        ),
    ]
