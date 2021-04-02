# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0032_add_french_ws'),
    ]

    operations = [
    migrations.RenameModel(
            old_name='English_WG',
            new_name='English_American_WG',
        ),
        migrations.RenameModel(
            old_name='English_WS',
            new_name='English_American_WS',
        ),
        migrations.RenameModel(
            old_name='Australian_English_WS',
            new_name='English_Australian_WS',
        ),
        migrations.RemoveField(
            model_name='russian_wg',
            name='item_456',
        ),
        migrations.AlterField(
            model_name='italian_wg',
            name='item_289',
            field=models.CharField(max_length=11, null=True, choices=[('understands', 'understands'), ('produces', 'produces')]),
        ),
        migrations.AlterField(
            model_name='russian_wg',
            name='item_27',
            field=models.CharField(max_length=9, null=True, choices=[('not yet', 'not yet'), ('sometimes', 'sometimes'), ('often', 'often')]),
        ),
        migrations.AlterField(
            model_name='russian_wg',
            name='item_28',
            field=models.CharField(max_length=9, null=True, choices=[('not yet', 'not yet'), ('sometimes', 'sometimes'), ('often', 'often')]),
        ),
    ]
