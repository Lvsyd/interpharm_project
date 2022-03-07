from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('domov', views.index, name='domov'),
    path('o-nas', views.o_nas, name='o-nas'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('sluzby', views.sluzby, name='sluzby'),
    path('zakaznicka-zona', views.zakaznicka_zona, name='zakaznicka-zona'),
    path('zastupujuce-znacky', views.zastupujuce_znacky, name='zastupujuce-znacky'),
]
