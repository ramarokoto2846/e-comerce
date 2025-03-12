from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Item

@receiver(pre_save, sender=Item)
def update_total_price(sender, instance, **kwargs):
    isinstance.total_price = float(instance.prod.prix) * isinstance.quantite