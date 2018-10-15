from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import SignUpForm
# Create your views here.
def registracija(request):
    if request.method!='POST':
        forma=SignUpForm()
    else:
        forma=SignUpForm(data=request.POST)
        if forma.is_valid():
            forma.save()
            return HttpResponseRedirect(reverse('login'))
    return render(request,'registracija.html',{'forma':forma})