from django.db import models

# Create your models here.
class categorias(models.Model):
    nombre_categoria=models.CharField(max_length=60)
   
def __str__(self):
    return '{}'.format(self.nombre_categoria)
     

