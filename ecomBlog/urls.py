from django.urls import path
from .views import index, inscription, connexion, connecte, deconnexion, panier, update_panier

urlpatterns = [
    path('', index, name="index_page"),
    path('inscription', inscription, name='inscription'),
    path('connexion', connexion, name='connexion'),
    path('deconnexion', deconnexion, name='deconnexion'),
    path('connecte', connecte, name='connecte'),
    path('panier', panier, name='pannier'),
    path('update_panier/<int:id>/', update_panier, name='update_panier'),
]