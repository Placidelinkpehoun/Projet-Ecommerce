from django import forms
from .models import Produit, Categories

class Add_Produit_Form(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['name', 'prix', 'categorie', 'img_produit']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mb-10', 'id': "name_produit", 'type': "text", 'placeholder': "Enter product name"}),
            'prix': forms.NumberInput(attrs={'class': 'mb-10', 'id': "quantite", 'type': "number", 'placeholder': "",}),
            #'auteur': forms.Select(attrs={'class': 'form-control', 'id': "auteur", 'type': "text", 'placeholder': "Auteur", 'data-sb-validations': "required"}),
            'categorie': forms.Select(attrs={'class': '', 'id': "categoriee", 'type': "text", 'placeholder': "Catégorie"}),
            'img_produit': forms.ClearableFileInput(attrs={'class': '', 'id': "image", 'type': "file", 'placeholder': ""}),
        }

class Add_Categorie_Form(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'img_categorie']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'flex-grow', 'id': "name_categorie", 'type': "text", 'placeholder': "Enter category name"}),
            #'img_categorie': forms.ClearableFileInput(attrs={'class': '', 'id': "image", 'type': "file", 'placeholder': ""}),
        }