# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('common', '0006_auto_20140501_2123')]

    operations = [
        migrations.AlterField(
            field = models.CharField(max_length=100),
            name = 'long_column',
            model_name = 'wordmapping',
        ),
    ]
