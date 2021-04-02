# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorySize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('production', models.IntegerField(null=True)),
                ('comprehension', models.IntegerField(null=True)),
                ('administration', models.ForeignKey(to='common.Administration', on_delete=models.CASCADE)),
            ],
        ),
    ]
