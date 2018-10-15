from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:planer_id>',views.obrisi,name='obrisi'),
    #path('<int:planer_id>/azuriranje',views.azuriraj,name='azuriraj'),
    path('<int:planer_id>/zavrsen',views.zavrsen,name='zavrsen'),
    path('obrisi_sve',views.obrisi_sve,name='obrisi_sve'),
]
