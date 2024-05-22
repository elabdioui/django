from django.contrib import admin
from .models import SignIn,SignUp
# Register your models here.

#recupération d'informations login dans la bdd
admin.site.register(SignIn)
admin.site.register(SignUp)
