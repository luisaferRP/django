from django import forms
from .models import productos

# creando lectura y mapeado de nuestro modelo apartir de la declaracion de el formulario

class productosForm(forms.ModelForm):
    class Meta:
        model=productos
        fields='__all__'
