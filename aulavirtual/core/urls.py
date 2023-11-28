from django.urls import path
from . import views #cuando pongo el punto me refiero al mismo directorio

urlpatterns = [
    path('', views.index, name='index') #url, nombre de la vista que lo atiende y un name
]
