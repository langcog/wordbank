# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20141217_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordmapping',
            name='lexical_category',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wordmapping',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
