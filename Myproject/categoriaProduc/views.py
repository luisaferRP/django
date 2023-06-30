from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from .models import categorias
from .forms import categoriasForm

# Creamos las vistas 
def inicio(request):
    return render(request,'inicio.html')

# def categorias(request):
#     return render(request,'categoria.html')

def categoria_crear(request):
    # preguntamos si lo de el formulario es valido y hacemos un redicionamiento
    formulario=categoriasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        # se redirecciona al index ya que alli tengo mi formuario
        return redirect('categoria')
        
    return render(request,'categoria/crearcate.html',{'formulario':formulario})

def categoria_editar(request,id):
    editar= categorias.objects.get(id=id)
    formulario= categoriasForm(request.POST or None, request.FILES or None, instance=editar)
    # preguntamos si esta el formulario y si hay un envio para hacer el guardado y redireccionar
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('categoria')
    
    return render(request,'editar.html', {'formulario': formulario})
    

def categoria_form(request):
    return render(request,'form.html',)

def categoria(request):
    index= categorias.objects.all()
    # a categorias le enviamos lo obtenido en la variable index
    return render (request,'categoria/categoria.html',{'categorias': index})

def eliminar(request,id):
    categoria = categorias.objects.get(id=id)
    categoria.delete()
    return redirect('categoria')
    



