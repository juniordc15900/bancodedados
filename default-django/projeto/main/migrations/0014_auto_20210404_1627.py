# Generated by Django 3.1.4 on 2021-04-04 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210404_1616'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='Fornecedor',
            new_name='Supplier',
        ),
    ]
