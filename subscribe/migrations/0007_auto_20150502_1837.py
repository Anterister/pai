# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0006_auto_20150502_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='referral',
            field=models.OneToOneField(default=None, to='anafero.Referral'),
            preserve_default=True,
        ),
    ]
