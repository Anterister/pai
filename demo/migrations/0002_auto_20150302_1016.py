# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailsubscriber',
            name='id',
        ),
        migrations.AlterField(
            model_name='emailsubscriber',
            name='email_addr',
            field=models.EmailField(max_length=75, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
