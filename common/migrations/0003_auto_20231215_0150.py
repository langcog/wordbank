# Generated by Django 3.1.14 on 2023-12-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20231215_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='source',
            field=models.CharField(blank=True, max_length=121, null=True),
        ),
    ]
