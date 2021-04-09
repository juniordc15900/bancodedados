# Generated by Django 3.1.2 on 2021-04-09 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField(default=0)),
                ('password', models.CharField(max_length=100)),
                ('cart', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MainDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content_html', models.TextField()),
                ('update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=100)),
                ('razao', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField(default=0)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('id_product', models.BigIntegerField()),
                ('price', models.FloatField()),
                ('quantity', models.BigIntegerField(default=0)),
                ('category', models.CharField(choices=[('comida', 'comida'), ('computador', 'computador'), ('livro', 'livro'), ('roupa', 'roupa'), ('movel', 'movel'), ('outros', 'outros')], default='comida', max_length=100)),
                ('supplier', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField()),
                ('validation', models.DateField()),
                ('security_code', models.BigIntegerField()),
                ('flag', models.CharField(choices=[('mastercard', 'mastercard'), ('elo', 'elo'), ('visa', 'visa'), ('carteirinha do RU', 'carteirinha do RU'), ('cielo', 'cielo')], default='mastercard', max_length=100)),
                ('client', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('number', models.BigIntegerField()),
                ('complement', models.CharField(max_length=100)),
                ('cep', models.BigIntegerField()),
                ('client', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
    ]
