from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.TextField(max_length=500, blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Paginas do Site

class Supplier(models.Model):
    cnpj = models.CharField(max_length=100)
    razao = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField(default=0)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.razao

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    id_product = models.BigIntegerField()
    price = models.FloatField()
    quantity = models.FloatField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,default=None)
    comida = 'comida'
    computador = 'computador'
    livro = 'livro'
    roupa = 'roupa'
    movel = "movel" 
    outros = "outros" 
    types_category = [
        (comida,'comida'),
        (computador,'computador'),
        (livro,'livro'),
        (roupa,'roupa'),
        (movel,'movel'),
        (outros,'outros'),
    ]
    category = models.CharField(
        max_length=100,
        choices=types_category,
        default=comida,
    )

    def __str__(self):
        return 'Fornecedor: '+self.supplier.razao+' Produto: '+self.name

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField(default=0)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Sell(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,default=None)
    conclude = models.BooleanField(default=0)
    timestamp = models.DateTimeField(auto_now=True)

class SellProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=None)
    quantity = models.IntegerField()  
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE,default=None)
    value = models.FloatField(default=0)
    real_value = models.FloatField(default=0)

class Address(models.Model):
    street = models.CharField(max_length=300) 
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    number = models.BigIntegerField()
    complement = models.CharField(max_length=100)
    cep = models.BigIntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return "Cliente: "+self.client.first_name+' cep: '+str(self.cep)

class Card(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,default=None)
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
    client = models.ForeignKey(Client, on_delete=models.CASCADE,default=None)

# Outros

class MainDocument(models.Model):
    title = models.CharField(max_length=200)
    content_html = models.TextField()
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title