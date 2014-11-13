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
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('study_id', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1, null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('birth_weight', models.FloatField(null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('gestational_age', models.IntegerField(null=True, blank=True)),
                ('mom_ed', models.IntegerField(null=True, blank=True)),
                ('dad_ed', models.IntegerField(null=True, blank=True)),
                ('birth_order', models.IntegerField(null=True, blank=True)),
                ('ethnicity', models.ForeignKey(to_field='id', blank=True, to='common.Ethnicity', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
