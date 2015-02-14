# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20150213_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='mom_ed',
        ),
        migrations.AddField(
            model_name='child',
            name='momed',
            field=models.ForeignKey(blank=True, to='common.MomEd', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='child',
            name='study_momed',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
