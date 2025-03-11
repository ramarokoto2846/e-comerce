from django.contrib import admin
from .models import Produit, Panier, PanierItem

# Register your models here.
admin.site.register(Produit)
admin.site.register(Panier)
admin.site.register(PanierItem)