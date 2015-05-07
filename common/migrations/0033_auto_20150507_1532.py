# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0032_auto_20150506_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentsmap',
            name='form',
            field=models.CharField(max_length=2, choices=[(b'WS', b'Words & Sentences'), (b'WG', b'Words & Gestures'), (b'TC', b'Toddler Checklist'), (b'IC', b'Infant Checklist')]),
            preserve_default=True,
        ),
    ]
