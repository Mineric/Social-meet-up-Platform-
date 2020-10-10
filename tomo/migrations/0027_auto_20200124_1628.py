# Generated by Django 2.2.5 on 2020-01-24 07:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tomo', '0026_auto_20200124_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 24, 7, 28, 6, 635352, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 24, 7, 28, 6, 635352, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='hosted_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 24, 7, 28, 6, 635352, tzinfo=utc)),
        ),
    ]
