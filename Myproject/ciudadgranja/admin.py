from django.contrib import admin
#informacion que va a utilizar y de donde
from .models import productos
#Administrativos de django que administra por defecto la base de datos 
# Registramos en el administrados el modelo de productos
admin.site.register(productos)