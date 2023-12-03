from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User
from django.contrib.auth import login, logout, authenticate
from contactos.models import *
from productos.models import *
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    contactos = Contactos.objects.all().count()
    productos = Productos.objects.all().count()
    usuarios = User.objects.all().count()
    return render(request, 'home.html', {
        'contactos': contactos,
        'productos': productos,
        'usuarios': usuarios
    })

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def crear_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                     password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectas'
            })
        else:
            login(request, user)
            return redirect('home')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        else:
            return render(request, 'registro.html', {
                'form': UserCreationForm,
                "error": 'Las contraseñas no coinciden'
            })