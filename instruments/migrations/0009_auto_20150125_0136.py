# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0008_auto_20141221_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danish_ws',
            name='basetable_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='instruments.BaseTable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='english_wg',
            name='basetable_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='instruments.BaseTable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='english_ws',
            name='basetable_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='instruments.BaseTable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='norwegian_wg',
            name='basetable_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='instruments.BaseTable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='norwegian_ws',
            name='basetable_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='instruments.BaseTable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spanish_wg',
            name='basetable_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='instruments.BaseTable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='spanish_ws',
            name='basetable_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='instruments.BaseTable'),
            preserve_default=True,
        ),
    ]
