from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.SimpleRouter()
router.register(r'', views.Producto, '')

urlpatterns = [
    path('', views.productos, name='productos'),
    path('api/', include(router.urls)),
    path("create/", views.create_productos, name='create_productos'),
    path('edit/<int:p_id>/', views.edit_producto, name='edit_productos'),
    path('delete/<int:p_id>/', views.delete_producto, name='delete_productos'),
    path('docs/', include_docs_urls(title='Productos API')),
]