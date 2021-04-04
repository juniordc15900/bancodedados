from django.contrib import admin
from . import models

admin.site.register(models.Cliente)
admin.site.register(models.Fornecedor)
admin.site.register(models.Product)
admin.site.register(models.Address)
admin.site.register(models.Card)



    