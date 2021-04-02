# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0005_bsl_wg'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BSL_WG',
            new_name='British_Sign_Language_WG',
        ),
    ]
