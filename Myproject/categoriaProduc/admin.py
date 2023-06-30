from django.contrib import admin

from .models import categorias
#Administrativos de django que administra por defecto la base de datos 
# Registramos en el administrador el modelo de productos 
admin.site.register(categorias)
