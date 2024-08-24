from django.urls import path
from .views import *

urlpatterns = [
    path('',listarTareas,name='listarTareas'),
    path('crear',crearTarea,name='crearTarea')
]