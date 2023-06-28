from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse



from .models import productos
from .forms import productosForm

# Creamos las vistas 
def inicio(request):
    return render(request,'inicio.html')

def categoria(request):
    return render(request,'categoria.html')

def crear(request):
    # preguntamos si lo de el formulario es valido y hacemos un redicionamiento
    formulario=productosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        # se redirecciona al index ya que alli tengo mi formuario
        return redirect('index')
        
    return render(request,'vistas/crear.html',{'formulario':formulario})

def editar(request,id):
    editar= productos.objects.get(id=id)
    formulario= productosForm(request.POST or None, request.FILES or None, instance=editar)
    # preguntamos si esta el formulario y si hay un envio para hacer el guardado y redireccionar
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    
    return render(request,'vistas/editar.html', {'formulario': formulario})
    

def form(request):
    return render(request,'vistas/form.html',)

def index(request):
    index= productos.objects.all()
    return render (request,'vistas/index.html',{'productos': index})

def eliminar(request,id):
    eliminar= productos.objects.get(id=id)
    eliminar.delete()
    return redirect('index')
    
