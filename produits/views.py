from pydoc import pager
from django.shortcuts import get_object_or_404, render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Vehicule

# Create your views here.

#la fonction qui englobe la totalitédes produit "produits" 
def totproduit(request):
   
    return render(request,'produit/totproduit.html',{'prods':Vehicule.objects.all()})

def seulproduit(request,id):
    vehicule = get_object_or_404(Vehicule, id=id)
    return render(request,'produit/seulproduit.html',{'prod':Vehicule}) #key value to be added 


def seulproduit(request):
    # Initialiser un dictionnaire pour stocker les filtres
    filters = {}
    
    # Récupérer les paramètres de requête s'ils existent
    name = request.GET.get('name')
    exist = request.GET.get('exist')
    prix = request.GET.get('prix')
    typ = request.GET.get('typ')
    category = request.GET.get('category')
    
    # Ajouter les filtres dynamiquement
    if name:
        filters['name'] = name
    if exist:
        filters['exist'] = exist
    if prix:
        filters['prix'] = prix
    if typ:
        filters['typ'] = typ
    if category:
        filters['category'] = category
    
    # Appliquer les filtres à la requête
    produits = Vehicule.objects.filter(**filters)
    
    # Passer les produits filtrés au template
    return render(request, 'produit/seulproduit.html', {'prod': produits})


     