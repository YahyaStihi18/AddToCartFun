# Generated by Django 3.0.7 on 2020-06-17 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200617_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
