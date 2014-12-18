# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20141215_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='instrument_language',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='instrumentsmap',
            old_name='name',
            new_name='form',
        ),
        migrations.AddField(
            model_name='source',
            name='instrument_form',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='source',
            name='citation',
        ),
        migrations.RemoveField(
            model_name='source',
            name='instrument',
        ),
    ]
