# Generated by Django 2.2.5 on 2020-01-22 14:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tomo.models


class Migration(migrations.Migration):

    dependencies = [
        ('tomo', '0014_auto_20200122_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_image',
            field=models.ImageField(default='default.jpg', upload_to=tomo.models.getUserImageFolder),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 22, 14, 9, 43, 140852, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='cover_image',
            field=models.ImageField(default='default.jpg', upload_to=tomo.models.getEventImageFolder),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 22, 14, 9, 43, 138892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='hosted_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 22, 14, 9, 43, 138892, tzinfo=utc)),
        ),
    ]
