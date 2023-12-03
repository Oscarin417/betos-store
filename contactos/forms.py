from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['nombre', 'correo', 'telefono', 'mensaje', 'condiciones']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
            'condiciones': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }