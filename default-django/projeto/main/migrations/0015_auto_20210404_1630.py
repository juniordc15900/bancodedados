# Generated by Django 3.1.4 on 2021-04-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210404_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cpf',
            field=models.CharField(max_length=100),
        ),
    ]
