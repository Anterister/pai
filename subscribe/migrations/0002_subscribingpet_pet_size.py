# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribingpet',
            name='pet_size',
            field=models.CharField(default='M', max_length=1, choices=[(b'S', b'Small'), (b'M', b'Midium'), (b'L', b'Large'), (b'X', b'Extra')]),
            preserve_default=False,
        ),
    ]
