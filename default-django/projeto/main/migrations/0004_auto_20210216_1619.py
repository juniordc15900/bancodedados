# Generated by Django 3.1.4 on 2021-02-16 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maindocuments',
            old_name='intro',
            new_name='content_html',
        ),
        migrations.RemoveField(
            model_name='maindocuments',
            name='update',
        ),
    ]
