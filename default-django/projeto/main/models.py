from django.db import models
# Paginas do Site
class HomePage(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

class AboutPage(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    
class ContactPage(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    endereco = models.TextField()
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=16)

class SiteDefault(models.Model):
    nome_da_empresa = models.CharField(max_length=100)
    logomarca = models.ImageField()
    cor_primaria = models.CharField(max_length=100)
    cor_secundaria = models.CharField(max_length=100) 
    cor_terciaria = models.CharField(max_length=100) 

# Outros
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title

class MainDocument(models.Model):
    title = models.CharField(max_length=200)
    content_html = models.TextField()
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title