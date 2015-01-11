# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20141226_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='mom_ed',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'nothing', b'nothing'), (b'primary', b'primary'), (b'some secondary', b'some secondary'), (b'secondary', b'secondary'), (b'some college', b'some college'), (b'college', b'college'), (b'some graduate', b'some graduate'), (b'graduate', b'graduate')]),
        ),
    ]
