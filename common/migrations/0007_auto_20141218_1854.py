# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20141218_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmapping',
            name='type',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='wordmapping',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='wordmapping',
            name='lexical_category',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
