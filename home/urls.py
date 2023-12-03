from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("registro/", views.registro, name='registro'),
    path("logout/", views.cerrar_sesion, name='logout'),
    path("login/", views.crear_sesion, name='login')
]