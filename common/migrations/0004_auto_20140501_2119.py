# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('common', '0003_auto_20140501_2033')]

    operations = [
        migrations.DeleteModel(
            'WordMapping',
        ),
        migrations.DeleteModel(
            'WordInfo',
        ),
    ]
