# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0029_auto_20150410_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='citation',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='contributor',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
