# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0033_auto_20150507_1532'),
    ]

    operations = [
        migrations.RenameModel('InstrumentsMap', 'Instrument'),
        migrations.CreateModel(
            name='ItemInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=50)),
                ('item_id', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=30)),
                ('definition', models.CharField(max_length=200, null=True, blank=True)),
                ('gloss', models.CharField(max_length=80, null=True, blank=True)),
                ('complexity_category', models.CharField(max_length=30, null=True, blank=True)),
                ('category', models.ForeignKey(to='common.Category', null=True)),
                ('instrument', models.ForeignKey(to='common.Instrument')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemMap',
            fields=[
                ('uni_lemma', models.CharField(max_length=50, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='WordInfo',
        ),
        migrations.DeleteModel(
            name='WordMapping',
        ),
    ]
