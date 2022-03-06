from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('domov', views.index, name='domov'),
    path('o-nas', views.o_nas, name='o-nas'),
]
