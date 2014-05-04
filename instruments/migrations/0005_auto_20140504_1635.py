# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('instruments', '0004_auto_20140504_1634')]

    operations = [
        migrations.RemoveField(
            name = u'id',
            model_name = 'wg',
        ),
        migrations.RemoveField(
            name = u'id',
            model_name = 'ws',
        ),
        migrations.AlterField(
            field = models.OneToOneField(auto_created=True, primary_key=True, to_field=u'id', serialize=False, to='instruments.BaseTable'),
            name = u'basetable_ptr',
            model_name = 'wg',
        ),
        migrations.AlterField(
            field = models.OneToOneField(auto_created=True, primary_key=True, to_field=u'id', serialize=False, to='instruments.BaseTable'),
            name = u'basetable_ptr',
            model_name = 'ws',
        ),
    ]
