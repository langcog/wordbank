# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_auto_20160920_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='license',
            field=models.CharField(default='CC-BY', max_length=15, choices=[(b'CC-BY', b'CC BY 4.0'), (b'CC-BY-NC', b'CC BY-NC 4.0')]),
            preserve_default=False,
        ),
    ]
