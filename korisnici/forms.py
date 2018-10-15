from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        labels={
            'first_name':'Ime',
            'last_name':'Prezime',
            'email':'Email Adresa',
        }
        fields = ('first_name','last_name','username', 'email', )
        widgets={'email':forms.TextInput(attrs={'required':'true'})}
        help_texts={'email':'Obavezno','username':'Obavezno. 150 karaktera ili manje. Slova, brojevi i @/./+/-/_ samo.',}