# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0028_auto_20150410_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentsmap',
            name='has_grammar',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
