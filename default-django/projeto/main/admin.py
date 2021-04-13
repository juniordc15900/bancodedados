from django.contrib import admin
from . import models

admin.site.register(models.Client)
admin.site.register(models.Supplier)
admin.site.register(models.Product)
admin.site.register(models.Address)
admin.site.register(models.Card)
admin.site.register(models.SellProduct)
admin.site.register(models.Sell)



    