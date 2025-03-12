from django.urls import path
from .views import index, inscription, connexion, connecte, deconnexion, panier, deleteItem, deletePanier, editItem, ajouterPanier

urlpatterns = [
    path('', index, name="index_page"),
    path('inscription', inscription, name='inscription'),
    path('connexion', connexion, name='connexion'),
    path('deconnexion', deconnexion, name='deconnexion'),
    path('connecte', connecte, name='connecte'),

    path('panier', panier, name='pannier'),
    path('panier/delete/', deletePanier, name='delete_panier'),

    path('panier/item/delete/<int:i_id>/', deleteItem, name='delete_item'),
    path('panier/item/edit/<int:i_id>/', editItem, name='edit_item'),

    path('panier/ajouter/<int:prod_id>/', ajouterPanier, name='ajouter_au_panier'),
]