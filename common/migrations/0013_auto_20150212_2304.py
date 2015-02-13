# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_auto_20150212_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='mom_ed',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'nothing', b'Nothing'), (b'primary', b'Primary'), (b'some secondary', b'Some Secondary'), (b'secondary', b'Secondary'), (b'some college', b'Some College'), (b'college', b'College'), (b'some graduate', b'Some Graduate'), (b'graduate', b'Graduate')]),
            preserve_default=True,
        ),
    ]
