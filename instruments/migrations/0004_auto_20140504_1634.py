# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('instruments', '0003_basetable')]

    operations = [
        migrations.AddField(
            field = models.IntegerField(null=True),
            name = 'basetable_ptr',
            model_name = 'wg',
        ),
        migrations.AddField(
            field = models.IntegerField(null=True),
            name = 'basetable_ptr',
            model_name = 'ws',
        ),
    ]
