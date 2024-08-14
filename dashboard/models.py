from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    id_categorie = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    img_categorie = models.ImageField(upload_to='front/images/category/', null=True, blank=True)
    def __str__(self):
        return self.name

class Produit(models.Model):
    id_produit = models.IntegerField(default=1, primary_key=True)
    name = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    #quantite = models.IntegerField(default=1)
    best_seller = models.BooleanField(default=False)
    tendance = models.BooleanField(default=False)
    vedette = models.BooleanField(default=False)
    discount_produit = models.BooleanField(default=False)
    img_produit = models.ImageField(upload_to='front/images/grocery/', null=True, blank=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"