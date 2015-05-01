# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_auto_20150322_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='pet_breed',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='pet_gender',
            field=models.CharField(max_length=1, choices=[(b'1', b'Male'), (b'0', b'Female')]),
            preserve_default=True,
        ),
    ]
