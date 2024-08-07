# Generated by Django 3.1.13 on 2022-04-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("instruments", "0018_auto_20220408_1321"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dutch_swingley",
            name="item_271",
            field=models.CharField(
                choices=[("understands", "understands"), ("produces", "produces")],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="dutch_swingley",
            name="item_299",
            field=models.CharField(
                choices=[("understands", "understands"), ("produces", "produces")],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="dutch_swingley",
            name="item_381",
            field=models.CharField(
                choices=[("understands", "understands"), ("produces", "produces")],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="dutch_wg",
            name="item_399",
            field=models.CharField(
                choices=[("understands", "understands"), ("produces", "produces")],
                max_length=14,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="dutch_wg",
            name="item_400",
            field=models.CharField(
                choices=[("understands", "understands"), ("produces", "produces")],
                max_length=11,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="dutch_wg",
            name="item_411",
            field=models.CharField(
                choices=[("understands", "understands"), ("produces", "produces")],
                max_length=12,
                null=True,
            ),
        ),
    ]
