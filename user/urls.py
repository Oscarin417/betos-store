from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('create/', views.create_usuario, name='create_usuario'),
    path('delete/<int:u_id>/', views.delete_usuario, name='delete_usuario'),
    path('edit/<int:u_id>/', views.edit_usuario, name='edit_usuario'),
]