# Generated by Django 3.1.4 on 2021-04-04 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210403_2354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='validate',
            new_name='validation',
        ),
    ]