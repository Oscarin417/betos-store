from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import * 
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from rest_framework import viewsets
from .serializer import ProductosSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class Producto(viewsets.ModelViewSet):
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()

@login_required
def productos(request):
    productos_list = Productos.objects.all()
    items_por_pagina = 5
    paginator = Paginator(productos_list, items_por_pagina)
    page = request.GET.get('page')
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)
    return render(request, 'productos.html', {'productos': productos})

def create_productos(request):
    if request.method == 'GET':
        return render(request, 'create_producto.html', {
            'form': ProductoForm
        })
    else:
        try:
            form = ProductoForm(request.POST, request.FILES)
            form.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'create_producto.html', {
                'form': form,
                'error': 'Ingresa datos validos'
            })

def delete_producto(request, p_id):
    producto = get_object_or_404(Productos, pk=p_id)
    imagen_path = producto.imagen.path
    if request.method == 'POST':
        producto.delete()
        if os.path.exists(imagen_path):
            os.remove(imagen_path)
        return redirect('productos')

def edit_producto(request, p_id):
    if request.method == 'GET':
        producto = get_object_or_404(Productos, pk=p_id)
        form = ProductoForm(instance=producto)
        return render(request, 'edit_productos.html', {
            'producto': producto,
            'form': form
        })
    else:
        try:
            producto = get_object_or_404(Productos, pk=p_id)
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            form.save()
            return redirect('productos')
        except ValueError:
            producto = get_object_or_404(Productos, pk=p_id)
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            return render(request, 'edit_productos.html', {
                'producto': producto,
                'form': form,
                'error': 'Ingresa datos válidos'
            })
