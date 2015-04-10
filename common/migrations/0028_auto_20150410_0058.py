# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0027_auto_20150409_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumentsmap',
            name='has_grammar',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wordmapping',
            name='category',
            field=models.ForeignKey(to='common.Category', null=True),
            preserve_default=True,
        ),
    ]
