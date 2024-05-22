from django.db import models

# Create your models here.

# stocker les produits

class Vehicule(models.Model):
    choix = [
        ('voiture','voiture'),
        ('moto','moto'),
    ]
    matricule=models.CharField(max_length=100)
    name = models.TextField() 
    image = models.ImageField(upload_to='PhotoDeVoiture/%y/%m/%d',default="")
    exist = models.BooleanField(default=True)
    prix=models.BigIntegerField(default=0)
    typ=models.CharField(max_length=100)
    marque=models.CharField(max_length=100)
    category=models.CharField(max_length=50, choices=choix)

    
#cette fonction permet l'affichage des """produits""" par leur nom dans la bdd ADMIN(facultative mais importante!!!)
    def __str__(self) :
        return self.name
#cette fonction permet l'affichage des """classe""" par leur nom dans la bdd ADMIN(facultative mais importante!!!)
    class Meta:
        verbose_name = 'vehicule'
        ordering=['prix']





