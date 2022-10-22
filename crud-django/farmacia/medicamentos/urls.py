from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('remedios',views.listadoRemedios),
    path('agregarRemedios',views.agregarRemedios)
    
]