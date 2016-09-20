# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_auto_20160920_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='form',
            field=models.CharField(max_length=12, choices=[(b'WS', b'Words & Sentences'), (b'WG', b'Words & Gestures'), (b'TC', b'Toddler Checklist'), (b'IC', b'Infant Checklist'), (b'TEDS Twos', b'TEDS Twos'), (b'TEDS Threes', b'TEDS Threes'), (b'FormA', b'FormA'), (b'FormBOne', b'FormBOne'), (b'FormBTwo', b'FormBTwo'), (b'FormC', b'FormC')]),
        ),
    ]
