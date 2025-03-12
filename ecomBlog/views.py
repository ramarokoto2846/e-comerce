from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Panier, Item
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    prod = Produit.objects.all()
    return render(request, 'index.html', {"prod": prod})


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

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


def connecte(request):
    prod = Produit.objects.all()
    return render(request, 'connecte.html', {"prod": prod})


def deconnexion(request):
    logout(request)
    return redirect('index_page')


def deleteItem(request, i_id):
    item = get_object_or_404(Item, id=i_id)
    item.delete()
    return redirect('pannier')


def ajouterPanier(request, prod_id):
    if request.user.is_authenticated:
        produit = get_object_or_404(Produit, id=prod_id)
        
        panier, created = Panier.objects.get_or_create(user=request.user)

        item, created_item = Item.objects.get_or_create(panier=panier, prod=produit)
        
        if not created_item:
            item.quantite += 1
            item.total_price = item.quantite * float(item.prod.prix)
            item.save()
        else:
            item.quantite = 1
            item.total_price = float(item.prod.prix)
            item.save()
        return redirect('connecte')

    else:
        messages.error(request, "Veuillez vous connecter pour ajouter des produits au panier.")
        return redirect('connexion')


def deletePanier(request):
    if request.user.is_authenticated:
        pan = get_object_or_404(Panier, user=request.user)
        item = Item.objects.filter(panier=pan)
        for i in item:
            i.delete()
        return redirect('pannier')
    

def panier(request):
    pan = get_object_or_404(Panier, user=request.user)
    item = Item.objects.filter(panier=pan)

    total_prix = 0

    for i in item:
        total_price_item = float(i.prod.prix)*i.quantite
        total_prix += total_price_item

    context = {
        'paniers': pan, 
        'items': item, 
        'total_price_panier':total_prix, 
    }

    return render(request, 'panier.html', context)

def editItem(request, i_id):
    item = get_object_or_404(Item, id=i_id)
    if request.method == "POST":
        q = request.POST['quantite']
        item = get_object_or_404(Item, id=i_id)
        item.quantite = int(q)
        item.total_price = float(item.prod.prix)*item.quantite
        item.save()
        return redirect('pannier')
    return render(request, 'update_item.html', {"item":item})
    