# Generated by Django 3.1.13 on 2022-07-02 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0033_auto_20220521_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finnish_WSShort',
            fields=[
                ('basetable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='instruments.basetable')),
                ('item_1', models.CharField(max_length=11, null=True)),
                ('item_8', models.CharField(max_length=11, null=True)),
                ('item_2', models.CharField(max_length=11, null=True)),
                ('item_4', models.CharField(max_length=11, null=True)),
                ('item_12', models.CharField(max_length=11, null=True)),
                ('item_33', models.CharField(max_length=11, null=True)),
                ('item_17', models.CharField(max_length=11, null=True)),
                ('item_37', models.CharField(max_length=11, null=True)),
                ('item_21', models.CharField(max_length=11, null=True)),
                ('item_44', models.CharField(max_length=11, null=True)),
                ('item_47', models.CharField(max_length=11, null=True)),
                ('item_59', models.CharField(max_length=11, null=True)),
                ('item_54', models.CharField(max_length=11, null=True)),
                ('item_64', models.CharField(max_length=11, null=True)),
                ('item_73', models.CharField(max_length=11, null=True)),
                ('item_76', models.CharField(max_length=11, null=True)),
                ('item_110', models.CharField(max_length=11, null=True)),
                ('item_82', models.CharField(max_length=11, null=True)),
                ('item_19', models.CharField(max_length=11, null=True)),
                ('item_114', models.CharField(max_length=11, null=True)),
                ('item_115', models.CharField(max_length=11, null=True)),
                ('item_117', models.CharField(max_length=11, null=True)),
                ('item_93', models.CharField(max_length=11, null=True)),
                ('item_131', models.CharField(max_length=11, null=True)),
                ('item_138', models.CharField(max_length=11, null=True)),
                ('item_154', models.CharField(max_length=11, null=True)),
                ('item_147', models.CharField(max_length=11, null=True)),
                ('item_162', models.CharField(max_length=11, null=True)),
                ('item_178', models.CharField(max_length=11, null=True)),
                ('item_179', models.CharField(max_length=11, null=True)),
                ('item_170', models.CharField(max_length=11, null=True)),
                ('item_189', models.CharField(max_length=11, null=True)),
                ('item_221', models.CharField(max_length=11, null=True)),
                ('item_248', models.CharField(max_length=11, null=True)),
                ('item_225', models.CharField(max_length=11, null=True)),
                ('item_228', models.CharField(max_length=11, null=True)),
                ('item_252', models.CharField(max_length=11, null=True)),
                ('item_253', models.CharField(max_length=11, null=True)),
                ('item_260', models.CharField(max_length=11, null=True)),
                ('item_237', models.CharField(max_length=11, null=True)),
                ('item_207', models.CharField(max_length=11, null=True)),
                ('item_216', models.CharField(max_length=11, null=True)),
                ('item_209', models.CharField(max_length=11, null=True)),
                ('item_219', models.CharField(max_length=11, null=True)),
                ('item_269', models.CharField(max_length=11, null=True)),
                ('item_272', models.CharField(max_length=11, null=True)),
                ('item_276', models.CharField(max_length=11, null=True)),
                ('item_296', models.CharField(max_length=11, null=True)),
                ('item_284', models.CharField(max_length=11, null=True)),
                ('item_596', models.CharField(max_length=11, null=True)),
                ('item_289', models.CharField(max_length=11, null=True)),
                ('item_320', models.CharField(max_length=11, null=True)),
                ('item_310', models.CharField(max_length=11, null=True)),
                ('item_329', models.CharField(max_length=11, null=True)),
                ('item_330', models.CharField(max_length=11, null=True)),
                ('item_339', models.CharField(max_length=11, null=True)),
                ('item_332', models.CharField(max_length=11, null=True)),
                ('item_340', models.CharField(max_length=11, null=True)),
                ('item_342', models.CharField(max_length=11, null=True)),
                ('item_349', models.CharField(max_length=11, null=True)),
                ('item_359', models.CharField(max_length=11, null=True)),
                ('item_360', models.CharField(max_length=11, null=True)),
                ('item_361', models.CharField(max_length=11, null=True)),
                ('item_400', models.CharField(max_length=11, null=True)),
                ('item_363', models.CharField(max_length=11, null=True)),
                ('item_415', models.CharField(max_length=11, null=True)),
                ('item_417', models.CharField(max_length=11, null=True)),
                ('item_382', models.CharField(max_length=11, null=True)),
                ('item_423', models.CharField(max_length=11, null=True)),
                ('item_425', models.CharField(max_length=11, null=True)),
                ('item_387', models.CharField(max_length=11, null=True)),
                ('item_388', models.CharField(max_length=11, null=True)),
                ('item_390', models.CharField(max_length=11, null=True)),
                ('item_430', models.CharField(max_length=11, null=True)),
                ('item_487', models.CharField(max_length=11, null=True)),
                ('item_472', models.CharField(max_length=11, null=True)),
                ('item_490', models.CharField(max_length=11, null=True)),
                ('item_480', models.CharField(max_length=11, null=True)),
                ('item_481', models.CharField(max_length=11, null=True)),
                ('item_518', models.CharField(max_length=11, null=True)),
                ('item_522', models.CharField(max_length=11, null=True)),
                ('item_524', models.CharField(max_length=11, null=True)),
                ('item_460', models.CharField(max_length=11, null=True)),
                ('item_466', models.CharField(max_length=11, null=True)),
                ('item_594', models.CharField(max_length=11, null=True)),
                ('item_590', models.CharField(max_length=11, null=True)),
                ('item_464', models.CharField(max_length=11, null=True)),
                ('item_538', models.CharField(max_length=11, null=True)),
                ('item_525', models.CharField(max_length=11, null=True)),
                ('item_537', models.CharField(max_length=11, null=True)),
                ('item_542', models.CharField(max_length=11, null=True)),
                ('item_553', models.CharField(max_length=11, null=True)),
                ('item_558', models.CharField(max_length=11, null=True)),
                ('item_560', models.CharField(max_length=11, null=True)),
                ('item_570', models.CharField(max_length=11, null=True)),
                ('item_581', models.CharField(max_length=11, null=True)),
                ('item_583', models.CharField(max_length=11, null=True)),
                ('item_591', models.CharField(max_length=11, null=True)),
                ('item_588', models.CharField(max_length=11, null=True)),
                ('item_593', models.CharField(max_length=11, null=True)),
            ],
            bases=('instruments.basetable',),
        ),
    ]