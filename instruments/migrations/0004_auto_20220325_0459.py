# Generated by Django 3.1.7 on 2022-03-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0003_irish_ws'),
    ]

    operations = [
        migrations.AddField(
            model_name='hebrew_ws',
            name='item_639',
            field=models.CharField(choices=[('understands', 'understands'), ('produces', 'produces')], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='hebrew_ws',
            name='item_640',
            field=models.CharField(choices=[('understands', 'understands'), ('produces', 'produces')], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='hebrew_ws',
            name='item_641',
            field=models.CharField(choices=[('understands', 'understands'), ('produces', 'produces')], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='hebrew_ws',
            name='item_642',
            field=models.CharField(choices=[('understands', 'understands'), ('produces', 'produces')], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='hebrew_ws',
            name='item_643',
            field=models.CharField(choices=[('understands', 'understands'), ('produces', 'produces')], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='hebrew_ws',
            name='item_644',
            field=models.CharField(choices=[('understands', 'understands'), ('produces', 'produces')], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='hebrew_ws',
            name='item_645',
            field=models.CharField(choices=[('understands', 'understands'), ('produces', 'produces')], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='hebrew_ws',
            name='item_646',
            field=models.CharField(choices=[('understands', 'understands'), ('produces', 'produces')], max_length=11, null=True),
        ),
    ]