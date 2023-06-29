from django import forms
from .models import productos

# creando lectura y mapeado de nuestro modelo apartir de la declaracion de el formulario

class productosForm(forms.ModelForm):
    class Meta:
        model=productos
        # usar todos los campos
        fields='__all__'
