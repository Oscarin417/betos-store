from rest_framework import serializers
from .models import Contactos

class ContactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        #fields = ('id' ,'nombre', 'correo', 'telefono', 'mensaje', 'condiciones')
        fields = '__all__'