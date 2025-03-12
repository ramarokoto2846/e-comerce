from django.db import models
from django.contrib.auth.models import User
import random
    
class Produit(models.Model):
    
    uid = models.CharField(
        max_length=10,
        editable=False,
        unique=True
    )   

    name = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits/', null=True, blank=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}_uid:{self.uid} {self.prix}"
    
    def save(self, *args, **kwargs):
        if not self.uid:
            uid = []
            re = ''
            for i in range(10):
                a = random.randint(0, 9)
                uid.append(a)

            for e in uid:
                e_str = str(e)
                re = re + e_str
            self.uid = re
        super().save(*args, **kwargs)



class Panier(models.Model):
    uid = models.CharField(
        max_length=10,
        editable=False,
        unique=True
    )
    user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_item_count(self):
        return self.panier.count()
    
    class Meta:
        unique_together = ('user',)
    

    def __str__(self):
        return f"{self.uid} {self.user} - {self.get_item_count} Itm"


    def save(self, *args, **kwargs):
        if not self.uid:
            uid = []
            re = ''
            for i in range(10):
                a = random.randint(0, 9)
                uid.append(a)

            for e in uid:
                e_str = str(e)
                re = re + e_str
            self.uid = re

        super().save(*args, **kwargs)



class Item(models.Model):
    panier = models.ForeignKey(Panier, related_name='panier', on_delete=models.CASCADE)
    prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    add_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = float(self.prod.prix)*self.quantite
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.panier.uid} {self.prod.name} - {self.quantite} pcs"