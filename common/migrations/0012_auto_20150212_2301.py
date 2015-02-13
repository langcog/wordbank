# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20150209_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='mom_ed',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Nothing', b'Nothing'), (b'Primary', b'Primary'), (b'Some Secondary', b'Some Secondary'), (b'Secondary', b'Secondary'), (b'Some College', b'Some College'), (b'College', b'College'), (b'Some Graduate', b'Some Graduate'), (b'Graduate', b'Graduate')]),
            preserve_default=True,
        ),
    ]
