from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import * 
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from .serializer import ContactosSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class Contacto(viewsets.ModelViewSet):
    serializer_class = ContactosSerializer
    queryset = Contactos.objects.all()

# Create your views here.
@login_required
def contacto(request):
    contactos_list = Contactos.objects.all()
    items_por_pagina = 5
    paginator = Paginator(contactos_list, items_por_pagina)
    page = request.GET.get('page')
    try:
        contactos = paginator.page(page)
    except PageNotAnInteger:
        contactos = paginator.page(1)
    except EmptyPage:
        contactos = paginator.page(paginator.num_pages)
    return render(request, 'contactos.html', {'contactos': contactos})

def create_contacto(request):
    if request.method == 'GET':
        return render(request, 'create_contacto.html', {
            'form': ContactoForm
        })
    else:
        try:
            form = ContactoForm(request.POST)
            form.save()
            return redirect('contactos')
        except ValueError:
            return render(request, 'create_contacto.html', {
                'form': ContactoForm,
                'error': 'Ingresa datos validos'
            })

def delete_contacto(request, c_id):
    contacto = get_object_or_404(Contactos, pk=c_id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('contactos')

def edit_contacto(request, c_id): 
    if request.method == 'GET':
        contacto = get_object_or_404(Contactos, pk=c_id)
        form = ContactoForm(instance=contacto)
        return render(request, 'edit_contacto.html', {
            'contacto': contacto,
            'form': form
        })
    else:
        try:
            contacto = get_object_or_404(Contactos, pk=c_id)
            form = ContactoForm(request.POST, instance=contacto)
            form.save()
            return redirect('contactos')
        except ValueError:
            contacto = get_object_or_404(Contactos, pk=c_id)
            form = ContactoForm(request.POST, instance=contacto)
            return render(request, 'edit_contacto.html', {
                'contacto': contacto,
                'form': form,
                'error': 'Ingresa datos validos'
            })