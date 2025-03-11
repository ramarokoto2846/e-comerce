from django.db import models
from django.contrib.auth.models import User
    
class Produit(models.Model):
    name = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits/', null=True, blank=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Panier(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Panier de {self.user.username}"

    def update_total(self):
        self.total = sum(item.quantite * item.prod.prix for item in self.items.all())
        self.save()

class PanierItem(models.Model):
    panier = models.ForeignKey(Panier, related_name='items', on_delete=models.CASCADE)
    prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.prod.name} - {self.quantite} pcs"
