# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_category_lexical_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='study_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
