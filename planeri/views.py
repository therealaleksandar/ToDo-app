from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from .forms import PlanerAzuriranje
from .models import Planer
# Create your views here.
@login_required
def home(request):
    autor=request.user
    planeri=Planer.objects.all().filter(autor=autor)
    if request.method!='POST':
        forma=PlanerAzuriranje()
    else:
        forma=PlanerAzuriranje(data=request.POST)
        if forma.is_valid():
            novi_planer=forma.save(commit=False)
            novi_planer.autor=autor
            novi_planer.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request,'home.html',{'planeri':planeri,'forma':forma})

@login_required
def obrisi(request,planer_id):
    planer=Planer.objects.get(id=planer_id)
    proveri_autora(request,planer)
    planer.delete()
    return HttpResponseRedirect(reverse_lazy('home'))

@login_required
def zavrsen(request,planer_id):
    planer=Planer.objects.get(id=planer_id)
    proveri_autora(request,planer)
    planer.zavrsen=True
    planer.save()
    return HttpResponseRedirect(reverse_lazy('home'))

# @login_required
# def azuriraj(request,planer_id):
#     planer=Planer.objects.get(id=planer_id)
#     proveri_autora(request,planer)
#     if request.method!='POST':
#         forma=PlanerAzuriranje(instance=planer)
#     else:
#         forma=PlanerAzuriranje(instance=planer,data=request.POST)
#         if forma.is_valid():
#             forma.save()
#             return HttpResponseRedirect(reverse('home'))
#     context={'forma':forma}
#     return render(request,'planer_detaljno.html',context)

@login_required
def obrisi_sve(request):
    planeri=Planer.objects.filter(zavrsen=True).all()
    planeri.delete()
    return HttpResponseRedirect(reverse_lazy('home'))

def proveri_autora(request,planer):
    if request.user!=planer.autor:
        raise Http404
