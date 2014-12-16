# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20141205_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='ethnicity',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'A', b'Asian'), (b'B', b'Black'), (b'H', b'Hispanic'), (b'W', b'White'), (b'O', b'Other/Mixed')]),
        ),
    ]
