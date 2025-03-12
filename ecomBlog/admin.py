from django.contrib import admin
from .models import Produit, Panier, Item

# Register your models here.
class ProduitView(admin.ModelAdmin):
    
    def get_list_display(self, request):
        return [field.name for field in Produit._meta.fields]

class PanierView(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Panier._meta.fields]

class ItemView(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Item._meta.fields]


admin.site.register(Produit, ProduitView)
admin.site.register(Panier, PanierView)
admin.site.register(Item, ItemView)