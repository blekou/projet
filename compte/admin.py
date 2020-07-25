from django.contrib import admin
from .models import Produit
from .import models

admin.site.register(models.Client)
admin.site.register(models.Produit)
admin.site.register(models.Commande)
admin.site.register(models.Tag)


class ProduitAdmin(admin.ModelAdmin):
    pass



