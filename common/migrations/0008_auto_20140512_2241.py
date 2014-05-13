# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('common', '0007_auto_20140501_2125')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('ethnicity', models.CharField(max_length=30),)],
            bases = (models.Model,),
            options = {},
            name = 'Ethnicity',
        ),
        migrations.AddField(
            field = models.ForeignKey(to_field=u'id', blank=True, to='common.Ethnicity', null=True),
            name = 'ethnicity',
            model_name = 'child',
        ),
        migrations.RemoveField(
            name = 'year',
            model_name = 'source',
        ),
        migrations.AlterField(
            field = models.CharField(max_length=50),
            name = 'name',
            model_name = 'source',
        ),
    ]
