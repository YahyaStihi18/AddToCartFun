# Generated by Django 3.0.7 on 2020-06-17 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_orderitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='item',
        ),
    ]