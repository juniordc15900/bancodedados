# Generated by Django 3.1.4 on 2021-04-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_client_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='custom/img/', width_field='width_field'),
        ),
    ]
