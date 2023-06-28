from django.db import models
# from categoriaProduc.models import categorias

# Create your models here.
class productos(models.Model):
    id=models.CharField(max_length=60 ,primary_key=True)
    nombre=models.CharField(max_length=30, verbose_name='Nombre')
    descripcion=models.CharField(max_length=100, verbose_name='Descripcion')
    #Verbose nos muestra para mostrarle al usuario como se llama el campo (label)
    valor_producto=models.CharField(max_length=100, verbose_name='Valor')
    fecha_ingreso=models.DateField()
    # categorias=models.ForeingKey(categorias,null=True,blanck=True,on_dele=models.CASCADE)

    def _str_(self):
        fila = "Nombre:" + self.nombre + "-" + "Valor:" + self.valor_producto
        return fila
    




