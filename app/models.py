from django.db import models

# Create your models here.

#pour stocker les données

#classe de SIGNIN
class SignIn(models.Model):
    mail = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

#classe de SIGNUP
class SignUp(models.Model):
    usernname = models.CharField(max_length=150)
    mail = models.CharField(max_length=350)
    password = models.CharField(max_length=150)
