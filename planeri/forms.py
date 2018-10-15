from django.forms import ModelForm
from django import forms
from .models import Planer

class PlanerAzuriranje(ModelForm):
    class Meta:
        model=Planer
        fields=['tekst']
        labels={'tekst':''}
        widgets={'tekst':forms.TextInput(attrs={'placeholder':'npr. Procitam knjigu'})}
        help_texts={'tekst':"Pritisnite 'enter' da bi ste dodali va&#353u &#382elju."}
