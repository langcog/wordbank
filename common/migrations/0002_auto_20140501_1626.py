# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('common', '0001_initial')]

    operations = [
        migrations.AlterField(
            field = models.IntegerField(null=True, blank=True),
            name = 'age',
            model_name = 'administration',
        ),
    ]
