from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.SimpleRouter()
router.register(r'', views.Contacto, '')

urlpatterns = [
    path('', views.contacto, name='contactos'),
    path("create/", views.create_contacto, name='create_contactos'),
    path('edit/<int:c_id>/', views.edit_contacto, name='edit_contactos'),
    path('delete/<int:c_id>/', views.delete_contacto, name='delete_contactos'),
    path('api/', include(router.urls)),
    path('delete/<int:c_id>/', views.delete_contacto, name='delete_contactos'),
    path('docs/', include_docs_urls(title='Contactos API')),
]