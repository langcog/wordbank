# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordmapping',
            name='item',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='wordmapping',
            name='column',
        ),
    ]
