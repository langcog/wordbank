# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_remove_source_norming'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='study_family_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='zygosity',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'M', b'Monozygotic'), (b'D', b'Dizygotic')]),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='form',
            field=models.CharField(max_length=12, choices=[(b'WS', b'Words & Sentences'), (b'WG', b'Words & Gestures'), (b'TC', b'Toddler Checklist'), (b'IC', b'Infant Checklist'), (b'TEDS Twos', b'TEDS Twos'), (b'TEDS Threes', b'TEDS Threes')]),
        ),
    ]
