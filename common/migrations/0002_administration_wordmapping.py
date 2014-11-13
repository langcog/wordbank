# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('child', models.ForeignKey(to='common.Child', to_field='id')),
                ('instrument', models.ForeignKey(to='common.InstrumentsMap', to_field='id')),
                ('source', models.ForeignKey(to_field='id', blank=True, to='common.Source', null=True)),
                ('date_of_test', models.DateField(null=True, blank=True)),
                ('data_id', models.IntegerField()),
                ('age', models.IntegerField(null=True, blank=True)),
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
