from django.urls import include,re_path,path
from . import views

# importamos propiedades(clases) para acceder (MEDIA_URL)
from django.conf import settings
# ruta estatica que se requiere
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static

#Ingresamos a las vistas creadas
urlpatterns = [
    path(r'',views.inicio,name='inicio'),
    path(r'categoria/editar/',views.categoria_editar,name='categoria_editar'),
    path(r'categoria/crear/',views.categoria_crear,name='categoria_crear'),
     path(r'categoria/form/',views.categoria_form,name='categoria_form'),
    # llamamos la direccion y le pasamos un dato para borrar con el id
    # path(r'',views.inicio,name='inicio'),
    path(r'categoria',views.categoria,name='categoria'),
    # # llamamos la direccion y le pasamos un dato para borrar con el id
    path(r'eliminar/<id>/',views.eliminar, name='eliminar'),
    path(r'editar/<id>/',views.categoria_editar, name='categoria_editar'),


]