from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import UserForm 
from .models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def usuarios(request):
    usuarios_list = User.objects.all()
    items_por_pagina = 5
    paginator = Paginator(usuarios_list, items_por_pagina)
    page = request.GET.get('page')
    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        usuarios = paginator.page(1)
    except EmptyPage:
        usuarios = paginator.page(paginator.num_pages)
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def create_usuario(request):
    if request.method == 'GET':
        return render(request, 'create_usuarios.html', {
            'form': UserForm
        })
    else:
        try:
            form = UserForm(request.POST, request.FILES)
            form.save()
            return redirect('usuarios')
        except ValueError:
            return render(request, 'create_usuarios.html', {
                'form': UserForm,
                'error': 'Ingresa datos validos'
            })

def delete_usuario(request, u_id):
    usuario = get_object_or_404(User, pk=u_id)
    if request.method == 'POST':
        usuario.delete()
        if os.path.exists(imagen_path):
            os.remove(imagen_path)
        return redirect('usuarios')

def edit_usuario(request, u_id): 
    if request.method == 'GET':
        usuario = get_object_or_404(User, pk=u_id)
        form = UserForm(instance=usuario)
        return render(request, 'edit_usuarios.html', {
            'usuario': usuario,
            'form': form
        })
    else:
        try:
            usuario = get_object_or_404(User, pk=u_id)
            form = UserForm(request.POST, request.FILES, instance=usuario)
            form.save()
            return redirect('usuarios')
        except ValueError:
            usuario = get_object_or_404(User, pk=u_id)
            form = UserForm(request.POST, request.FILES, instance=usuario)
            return render(request, 'edit_usuarios.html', {
                'usuario': usuario,
                'form': form,
                'error': 'Ingresa datos validos'
            })