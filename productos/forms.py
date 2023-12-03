from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'precio', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'})
        }