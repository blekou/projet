from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user      = models.OneToOneField(User, null=True, blank="True", on_delete=models.CASCADE)
    nom       = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    email     = models.EmailField(max_length=200)
    date_add  = models.DateTimeField(auto_now_add=True)
    myprofile = models.ImageField(default="profil.png", null=True, blank=True)


    def __str__(self):
        return self.nom


class Tag(models.Model):
    
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom



class Produit(models.Model):
    
    CATEGORIE =(
       ( 'interieur' , 'interieur'),
       ( 'exterieur' , 'exterieur'),

    )
    nom = models.CharField(max_length=200)
    prix = models.FloatField(null =True)
    description = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200,choices=CATEGORIE)
    tags      = models.ManyToManyField(Tag,related_name="tag")
    date_add  = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nom

class Commande(models.Model):


    Status =(
       ( 'en attente' , 'en attente'),
       ( 'livrer','livrer'),
       ( 'commande total' ,'commande total'),

    )
    
    client   = models.ForeignKey(Client, on_delete = models.CASCADE)
    produit  = models.ForeignKey(Produit, on_delete = models.CASCADE)
    status   = models.CharField(max_length=200, null=True, choices = Status)
    date_add = models.DateTimeField(auto_now_add=True)
    nombre_produit = models.FloatField(null =True)
    prix = models.FloatField(null =True)



    def __str__(self):
        return self.produit.nom 

    