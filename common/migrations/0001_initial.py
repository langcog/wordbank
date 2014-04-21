# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('study_id', models.CharField(max_length=20),), ('gender', models.CharField(max_length=1),), ('date_of_birth', models.DateField(null=True, blank=True),), ('birth_weight', models.FloatField(null=True, blank=True),), ('state', models.CharField(max_length=2, null=True, blank=True),), ('gestational_age', models.IntegerField(null=True, blank=True),), ('mom_ed', models.IntegerField(null=True, blank=True),), ('dad_ed', models.IntegerField(null=True, blank=True),), ('birth_order', models.IntegerField(null=True, blank=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Child',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=20),), ('language', models.CharField(max_length=20),)],
            bases = (models.Model,),
            options = {},
            name = 'InstrumentsMap',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('lemma', models.CharField(max_length=20),), ('instrument', models.IntegerField(),), ('short_column', models.CharField(max_length=8),), ('long_column', models.CharField(max_length=20),)],
            bases = (models.Model,),
            options = {},
            name = 'WordMapping',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=20),), ('citation', models.CharField(max_length=20),), ('year', models.IntegerField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Source',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('lemma', models.CharField(max_length=20),), ('CDI_cat', models.CharField(max_length=20),)],
            bases = (models.Model,),
            options = {},
            name = 'WordInfo',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('child', models.ForeignKey(to='common.Child', to_field=u'id'),), ('instrument', models.ForeignKey(to='common.InstrumentsMap', to_field=u'id'),), ('source', models.ForeignKey(to_field=u'id', blank=True, to='common.Source', null=True),), ('date_of_test', models.DateField(null=True, blank=True),), ('data_id', models.IntegerField(),), ('age', models.IntegerField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Administration',
        ),
    ]
