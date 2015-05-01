# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoxSubscriber',
            fields=[
                ('login_email', models.EmailField(max_length=75, serialize=False, primary_key=True)),
                ('login_pswd', models.CharField(max_length=50)),
                ('s_phonenumber', models.CharField(max_length=20)),
                ('s_name', models.CharField(max_length=20)),
                ('s_address', models.CharField(max_length=50)),
                ('s_zipcode', models.CharField(max_length=15)),
                ('s_district', models.CharField(max_length=15)),
                ('s_city', models.CharField(max_length=15)),
                ('s_province', models.CharField(max_length=15)),
                ('s_note', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubscribingPet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pet_name', models.CharField(max_length=30)),
                ('pet_birthday', models.DateField(null=True, blank=True)),
                ('pet_gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubscribingSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcribing_duration', models.CharField(max_length=1, choices=[(b'1', b'OneMonth'), (b'3', b'ThreeMonths'), (b'6', b'SixMonths'), (b'12', b'OneYear')])),
                ('subscriber', models.ForeignKey(to='subscribe.BoxSubscriber')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='boxsubscriber',
            name='s_pet',
            field=models.ForeignKey(to='subscribe.SubscribingPet'),
            preserve_default=True,
        ),
    ]
