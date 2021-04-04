from django.db import models
from django import forms

# Paginas do Site
    
class Cliente(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.BigIntegerField()
    email = models.EmailField()
    phone = models.BigIntegerField(default=0)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=100)
    razao = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField(default=0)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+" "+self.last_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    id_product = models.BigIntegerField()
    price = models.CharField(max_length=10) 

class Address(models.Model):
    street = models.CharField(max_length=300) 
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    number = models.BigIntegerField()
    cep = models.BigIntegerField()

class Card(models.Model):

    number = models.BigIntegerField()
    validation = models.DateField()
    security_code = models.BigIntegerField()
    mastercard = 'mastercard'
    elo = 'elo'
    visa = 'visa'
    carteirinhaRU = 'carteirinha do RU'
    cielo = "cielo" 
    types_flag = [
        (mastercard,'mastercard'),
        (elo,'elo'),
        (visa,'visa'),
        (carteirinhaRU,'carteirinha do RU'),
        (cielo,'cielo'),
    ]
    flag = models.CharField(
        max_length=100,
        choices=types_flag,
        default=mastercard,
    )





# Outros

class MainDocument(models.Model):
    title = models.CharField(max_length=200)
    content_html = models.TextField()
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title