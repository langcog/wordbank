# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('common', '0005_wordinfo_wordmapping')]

    operations = [
        migrations.AlterField(
            field = models.CharField(max_length=40),
            name = 'long_column',
            model_name = 'wordmapping',
        ),
    ]
