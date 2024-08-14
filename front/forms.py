from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registration_Form(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': "name", 'type': "text", 'placeholder': "Name"}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'id': "email", 'type': "email", 'placeholder': "Email"}))
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(attrs={'id': "password", 'type': "password"}))
    #password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
   
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

