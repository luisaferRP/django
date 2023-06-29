from django.urls import include,re_path,path
from . import views
from .views import editar,eliminar

# importamos propiedades(clases) para acceder (MEDIA_URL)
from django.conf import settings
# ruta estatica que se requiere
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static

#Ingresamos a las vistas creadas
urlpatterns = [
    path(r'',views.inicio,name='inicio'),
    path(r'categorias',views.categoria,name='categoria'),
    path(r'editar',views.editar,name='editar'),
    path(r'crear',views.crear,name='crear'),
    path(r'form',views.form,name='form'),
    path(r'productos',views.index,name='index'),
    # llamamos la direccion y le pasamos un dato para borrar con el id
    path(r'eliminar/<id>',views.eliminar, name='eliminar'),
    path(r'editar/<id>/',views.editar, name='editar'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# media_url donde se encuentran las imagenes document es igual a la media root que creamos,con estos datos accedemos a los datos de las imagenes