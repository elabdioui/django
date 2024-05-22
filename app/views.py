from pydoc import pager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import SignIn,SignUp
from .forms import SignInForm,SignUpForm


# Create your views here.
# des fonctions pour retourner les pages html

def acceuil(request):
    return render(request,'pages/acceuil.html',)

def about(request):
    return render(request,'pages/about.html',)

def contacter(request):
    return render(request, 'pages/contact.html',)

def auth(request):
    #stocker les informations récuperer du form dans une seul variable
    infoSignIn=SignInForm(request.POST)
    # !!!important il faut toujours sauvgarder  
    infoSignIn.save()
    return render(request,'pages/auth.html',{'lf':infoSignIn})

def auth(request):
    signin_form = SignInForm()
    signup_form = SignUpForm()

    if request.method == 'POST':
        if 'signin' in request.POST:
            signin_form = SignInForm(request.POST)
            if signin_form.is_valid():
                # Traiter le formulaire de connexion
                signin_form.save()
                return redirect('acceuil')  # Rediriger après une connexion réussie
        elif 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                # Traiter le formulaire d'inscription
                signup_form.save()
                return redirect('acceuil')  # Rediriger après une inscription réussie

    return render(request, 'pages/auth.html', {'signin_form': signin_form, 'signup_form': signup_form})



