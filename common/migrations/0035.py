# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0034_auto_20150507_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminfo',
            name='map',
            field=models.ForeignKey(blank=True, to='common.ItemMap', null=True),
            preserve_default=True,
        ),
    ]
