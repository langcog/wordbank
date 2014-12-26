# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20141218_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmapping',
            name='definition',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
