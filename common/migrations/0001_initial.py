# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentsMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth_order', models.IntegerField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('ethnicity', models.CharField(blank=True, max_length=1, null=True, choices=[(b'A', b'Asian'), (b'B', b'Black'), (b'H', b'Hispanic'), (b'W', b'White')])),
                ('mom_ed', models.IntegerField(null=True, blank=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('study_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ethnicity', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('dataset', models.CharField(max_length=20, null=True, blank=True)),
                ('instrument', models.CharField(max_length=20, null=True, blank=True)),
                ('citation', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WordInfo',
            fields=[
                ('uni_lemma', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('lang_lemma', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('child', models.ForeignKey(to='common.Child', to_field='id')),
                ('instrument', models.ForeignKey(to='common.InstrumentsMap', to_field='id')),
                ('source', models.ForeignKey(to_field='id', blank=True, to='common.Source', null=True)),
                ('date_of_test', models.DateField(null=True, blank=True)),
                ('data_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('data_age', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WordMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column', models.CharField(max_length=8)),
                ('instrument', models.ForeignKey(to='common.InstrumentsMap', to_field='id')),
                ('category', models.CharField(max_length=20, null=True, blank=True)),
                ('definition', models.CharField(max_length=100)),
                ('word_info', models.ForeignKey(to='common.WordInfo', to_field=b'uni_lemma')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
