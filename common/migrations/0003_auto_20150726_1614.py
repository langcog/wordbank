# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_categorysize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorysize',
            name='administration',
        ),
        migrations.AddField(
            model_name='categorysize',
            name='data_id',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
