# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20141218_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordmapping',
            name='type',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wordmapping',
            name='word_info',
            field=models.ForeignKey(to_field=b'uni_lemma', blank=True, to='common.WordInfo', null=True),
        ),
        migrations.AlterField(
            model_name='wordmapping',
            name='definition',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wordmapping',
            name='lexical_category',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
