# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_test', models.DateField(null=True, blank=True)),
                ('data_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('data_age', models.IntegerField(null=True, blank=True)),
                ('production', models.IntegerField(null=True)),
                ('comprehension', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('lexical_category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('study_id', models.CharField(max_length=20)),
                ('birth_order', models.IntegerField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('ethnicity', models.CharField(blank=True, max_length=1, null=True, choices=[(b'A', b'Asian'), (b'B', b'Black'), (b'H', b'Hispanic'), (b'W', b'White'), (b'O', b'Other/Mixed')])),
                ('study_momed', models.CharField(max_length=100, null=True, blank=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
            ],
        ),
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
        ),
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
        ),
        migrations.CreateModel(
            name='ItemMap',
            fields=[
                ('uni_lemma', models.CharField(max_length=50, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='MomEd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=20, null=True, blank=True)),
                ('order', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('dataset', models.CharField(max_length=20, null=True, blank=True)),
                ('instrument_language', models.CharField(max_length=30)),
                ('instrument_form', models.CharField(max_length=20)),
                ('contributor', models.TextField(blank=True)),
                ('citation', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='map',
            field=models.ForeignKey(blank=True, to='common.ItemMap', null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='momed',
            field=models.ForeignKey(blank=True, to='common.MomEd', null=True),
        ),
        migrations.AddField(
            model_name='administration',
            name='child',
            field=models.ForeignKey(to='common.Child'),
        ),
        migrations.AddField(
            model_name='administration',
            name='instrument',
            field=models.ForeignKey(to='common.Instrument'),
        ),
        migrations.AddField(
            model_name='administration',
            name='source',
            field=models.ForeignKey(blank=True, to='common.Source', null=True),
        ),
    ]
