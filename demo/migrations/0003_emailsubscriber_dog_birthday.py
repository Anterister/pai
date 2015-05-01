# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20150302_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsubscriber',
            name='dog_birthday',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
