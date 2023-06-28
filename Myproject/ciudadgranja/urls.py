from django.urls import include,re_path,path
from . import views
from .views import editar

#Ingresamos a las vistas creadas
urlpatterns = [
    path(r'',views.inicio,name='inicio'),
    path(r'categorias',views.categoria,name='categoria'),
    path(r'editar',views.editar,name='editar'),
    path(r'crear',views.crear,name='crear'),
    path(r'form',views.form,name='form'),
    path(r'productos',views.index,name='index'),
    path(r'eliminar/<id>',views.eliminar, name='eliminar'),
    path(r'editar/<id>/',views.editar, name='editar')
    
    # llamamos la direccion y le pasamos un dato para borrar
    # path(r'eliminar',views.eliminar,name='eliminar'),


    

]