# fichier créer par le developpeur
from django.urls import path
from . import views
from .models import Vehicule

urlpatterns =[
    path('',views.totproduit,name="totproduit"),
    path('totproduit/seulproduit',views.seulproduit,name="seulproduit"),
]