# Generated by Django 3.1.7 on 2021-11-26 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='data_content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='administration',
            name='data_id',
            field=models.PositiveIntegerField(db_index=True, null=True),
        ),
    ]