# Generated by Django 3.0.7 on 2020-06-17 11:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200617_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='date_added',
        ),
        migrations.AddField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 11, 35, 57, 593896, tzinfo=utc)),
        ),
    ]
