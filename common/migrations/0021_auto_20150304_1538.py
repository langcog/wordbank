# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0020_vocabularysize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='comprehension',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='administration',
            name='production',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
