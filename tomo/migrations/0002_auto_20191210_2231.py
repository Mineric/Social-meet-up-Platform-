# Generated by Django 2.2.5 on 2019-12-10 13:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tomo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 13, 31, 36, 261630, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='hosted_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 13, 31, 36, 261630, tzinfo=utc)),
        ),
    ]
