# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('anafero', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscribe', '0004_auto_20150416_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('being_referred', models.BooleanField(default=False)),
                ('total_referrals', models.IntegerField(default=0)),
                ('avail_free_boxes', models.IntegerField(default=0)),
                ('referral', models.OneToOneField(to='anafero.Referral')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
