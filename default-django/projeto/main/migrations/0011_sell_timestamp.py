# Generated by Django 3.1.2 on 2021-04-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_sellproduct_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
