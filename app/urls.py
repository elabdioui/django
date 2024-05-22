# fichier creer par developpeur qui contient le chemin de chaque fichier html
#importer depuis app/views
# ' ' signifie la premiere page depuis serveur


from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name="acceuil"),
    path('contacter/', views.contacter, name="contacter"),
    path('about/', views.about, name="about"),
    path('auth/', views.auth, name="auth"),
]