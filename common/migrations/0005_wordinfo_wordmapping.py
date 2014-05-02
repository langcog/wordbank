# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('common', '0004_auto_20140501_2119')]

    operations = [
        migrations.CreateModel(
            fields = [('lemma', models.CharField(max_length=20, serialize=False, primary_key=True),), ('CDI_cat', models.ForeignKey(to='common.CDICategory', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'WordInfo',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('word_info', models.ForeignKey(to='common.WordInfo', to_field='lemma'),), ('instrument', models.ForeignKey(to='common.InstrumentsMap', to_field=u'id'),), ('short_column', models.CharField(max_length=8),), ('long_column', models.CharField(max_length=20),)],
            bases = (models.Model,),
            options = {},
            name = 'WordMapping',
        ),
    ]
