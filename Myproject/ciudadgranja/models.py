from typing import Any, Dict, Tuple
from django.db import models
from django.core.files.storage import default_storage
# from categoriaProduc.models import categorias

# Create your models here.
class productos(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30, verbose_name='Nombre')
    descripcion=models.CharField(max_length=100, null=True, verbose_name='Descripcion')
    imagen=models.ImageField(upload_to='imagenes/',null=True)
    #Verbose nos muestra para mostrarle al usuario como se llama el campo (label)
    valor_producto=models.CharField(max_length=100, verbose_name='Valor')
    #le indico que el campo se llene automáticamente con la fecha y hora actual cuando se cree un nuevo producto.
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    # categorias=models.ForeingKey(categorias,null=True,blanck=True,on_dele=models.CASCADE)

    def _str_(self):
        fila = "Nombre:" + self.nombre + "-" + "Descripcion:" + self.descripcion
        return fila
    
    # borrar imagen tambien en el storage
    def delete(self, using=None, keep_parents=False):
    # Agarramos la imagen accedemos al storage y borramos lo guardado en el storage con el mismo nombre de la imagen
        self.imagen.storage.delete(self.imagen.name)
        super().delete()




