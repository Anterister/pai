# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscribe', '0002_subscribingpet_pet_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_gift', models.BooleanField(default=False)),
                ('subscription_size', models.CharField(max_length=1, choices=[(b'S', b'Small'), (b'M', b'Midium'), (b'L', b'Large'), (b'X', b'Extra')])),
                ('subscription_plan', models.CharField(max_length=1, choices=[(b'1', b'OneMonth'), (b'3', b'ThreeMonths'), (b'6', b'SixMonths'), (b'12', b'OneYear')])),
                ('pet_name', models.CharField(max_length=30)),
                ('pet_birthday', models.DateField(null=True, blank=True)),
                ('pet_gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('s_phonenumber', models.CharField(max_length=20)),
                ('s_name', models.CharField(max_length=20)),
                ('s_address', models.CharField(max_length=50)),
                ('s_zipcode', models.CharField(max_length=15)),
                ('s_district', models.CharField(max_length=15)),
                ('s_city', models.CharField(max_length=15)),
                ('s_province', models.CharField(max_length=15)),
                ('s_note', models.CharField(max_length=50)),
                ('subscriber', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubscriptionRecord',
            fields=[
                ('order_id', models.IntegerField(serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid_at', models.DateField(null=True, blank=True)),
                ('dispatched_at', models.DateField(null=True, blank=True)),
                ('tracking_info', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='boxsubscriber',
            name='s_pet',
        ),
        migrations.DeleteModel(
            name='SubscribingPet',
        ),
        migrations.RemoveField(
            model_name='subscribingsession',
            name='subscriber',
        ),
        migrations.DeleteModel(
            name='BoxSubscriber',
        ),
        migrations.DeleteModel(
            name='SubscribingSession',
        ),
    ]
