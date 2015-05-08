# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0033_auto_20150507_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=30)),
                ('form', models.CharField(max_length=2, choices=[(b'WS', b'Words & Sentences'), (b'WG', b'Words & Gestures'), (b'TC', b'Toddler Checklist'), (b'IC', b'Infant Checklist')])),
                ('age_min', models.IntegerField()),
                ('age_max', models.IntegerField()),
                ('has_grammar', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        # migrations.CreateModel(
        #     name='ItemInfo',
        #     fields=[
        #         ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
        #         ('item', models.CharField(max_length=50)),
        #         ('item_id', models.CharField(max_length=20)),
        #         ('type', models.CharField(max_length=30)),
        #         ('definition', models.CharField(max_length=200, null=True, blank=True)),
        #         ('gloss', models.CharField(max_length=80, null=True, blank=True)),
        #         ('complexity_category', models.CharField(max_length=30, null=True, blank=True)),
        #         ('category', models.ForeignKey(to='common.Category', null=True)),
        #         ('instrument', models.ForeignKey(to='common.Instrument')),
        #     ],
        #     options={
        #     },
        #     bases=(models.Model,),
        # ),
        # migrations.CreateModel(
        #     name='ItemMap',
        #     fields=[
        #         ('uni_lemma', models.CharField(max_length=50, serialize=False, primary_key=True)),
        #     ],
        #     options={
        #     },
        #     bases=(models.Model,),
        # ),
        # migrations.RemoveField(
        #     model_name='wordmapping',
        #     name='category',
        # ),
        # migrations.RemoveField(
        #     model_name='wordmapping',
        #     name='instrument',
        # ),
        # migrations.RemoveField(
        #     model_name='wordmapping',
        #     name='word_info',
        # ),
        # migrations.DeleteModel(
        #     name='WordInfo',
        # ),
        # migrations.DeleteModel(
        #     name='WordMapping',
        # ),
        # migrations.AddField(
        #     model_name='iteminfo',
        #     name='map',
        #     field=models.ForeignKey(blank=True, to='common.ItemMap', null=True),
        #     preserve_default=True,
        # ),
        # migrations.AlterField(
        #     model_name='administration',
        #     name='instrument',
        #     field=models.ForeignKey(to='common.Instrument'),
        #     preserve_default=True,
        # ),
        # migrations.DeleteModel(
        #     name='InstrumentsMap',
        # ),
    ]
