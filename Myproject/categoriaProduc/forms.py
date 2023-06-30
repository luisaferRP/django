from django import forms
from .models import categorias

# creando lectura y mapeado de nuestro modelo apartir de la declaracion de el formulario

class categoriasForm(forms.ModelForm):
    class Meta:
        model=categorias
        # usar todos los campos
        fields='__all__'