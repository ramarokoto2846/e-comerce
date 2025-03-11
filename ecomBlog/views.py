from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Panier, PanierItem
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Créer votre vue pour afficher l'index
def index(request):
    prod = Produit.objects.all()
    return render(request, 'index.html', {"prod": prod})

# Inscription
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

# Connexion de l'utilisateur
def connexion(request):
    if request.method == 'POST':
        nomuser = request.POST['nom_user']
        motdepass = request.POST['passswrd']
        user = authenticate(request, username=nomuser, password=motdepass)
        if user is not None:
            login(request, user)
            return redirect('connecte')
        else:
            context = {'em': "Nom d'utilisateur ou mot de passe incorrect."}
            return render(request, 'index.html', context)
    return render(request, 'connexion.html')

# Page de connexion réussie
def connecte(request):
    prod = Produit.objects.all()
    return render(request, 'connecte.html', {"prod": prod})

# Déconnexion de l'utilisateur
def deconnexion(request):
    logout(request)
    return redirect('index_page')

# Affichage du panier
def panier(request):
    if request.user.is_authenticated:
        # Récupérer tous les produits associés à l'utilisateur dans son panier
        paniers = PanierItem.objects.filter(panier=request.user)

        if not paniers:
            context = {'message': "Votre panier est vide."}
            return render(request, 'panier.html', context)

        # Calculer le total global du panier
        total_panier = 0
        for panier_item in paniers:
            # Calculer le prix total pour chaque item (prix * quantité)
            panier_item.total_price_item = float(panier_item.prod.prix) * panier_item.quantite
            total_panier += panier_item.total_price_item

        return render(request, 'panier.html', {'paniers': paniers, 'total_panier': total_panier})
    else:
        return redirect('connexion')  # Si l'utilisateur n'est pas connecté, redirige vers la connexion

# Mise à jour du panier
def update_panier(request, id):
    panier = get_object_or_404(Panier, id=id)

    if request.method == 'POST':
        for item in panier.items.all():  # Supposons que panier.items fait référence aux produits dans le panier
            quantite = request.POST.get(f'quantite_{item.id}')
            if quantite:
                try:
                    quantite = int(quantite)
                    if quantite > 0:
                        item.quantite = quantite
                        item.save()
                except ValueError:
                    messages.error(request, f"Quantité invalide pour le produit {item.prod.name}.")
                    return redirect('update_panier', id=id)

        # Recalculer le total du panier après modification
        panier.total = sum(item.quantite * item.prod.prix for item in panier.items.all())
        panier.save()

        # Rediriger vers la page du panier avec un message de succès
        messages.success(request, "Le panier a été mis à jour avec succès.")
        return redirect('panier')  # Remplacez 'panier' par l'URL appropriée pour afficher le panier

    return render(request, 'update_panier.html', {'panier': panier})
