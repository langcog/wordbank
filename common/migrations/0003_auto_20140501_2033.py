# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('common', '0002_auto_20140501_1626')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=20),)],
            bases = (models.Model,),
            options = {},
            name = 'CDICategory',
        ),
        migrations.AddField(
            field = models.ForeignKey(to='common.WordInfo', default=1, to_field=u'id'),
            preserve_default = False,
            name = 'word_info',
            model_name = 'wordmapping',
        ),
        migrations.RemoveField(
            name = 'lemma',
            model_name = 'wordmapping',
        ),
        migrations.AlterField(
            field = models.ForeignKey(to='common.CDICategory', to_field=u'id'),
            name = 'CDI_cat',
            model_name = 'wordinfo',
        ),
        migrations.AlterField(
            field = models.ForeignKey(to='common.InstrumentsMap', to_field=u'id'),
            name = 'instrument',
            model_name = 'wordmapping',
        ),
    ]
