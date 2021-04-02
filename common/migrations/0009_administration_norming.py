# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_source_longitudinal'),
    ]

    operations = [
        migrations.AddField(
            model_name='administration',
            name='norming',
            field=models.BooleanField(default=False),
        ),
    ]
