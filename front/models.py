from django.db import models
from dashboard.models import Produit
from django.contrib.auth.models import User

# Create your models here.
class Commande(models.Model):
    produits = models.ManyToManyField(Produit)
    date_commande = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Commande_Produit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
