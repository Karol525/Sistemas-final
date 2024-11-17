from django.shortcuts import render

from django.http import HttpResponse 
from django.template import Template, Context 
from django.template.loader import get_template 
import datetime

from .models import Productos
from .models import Categorias

# Create your views here.
def saludo(request): 
    return HttpResponse ("Probando funcionamiento") 

def principal(request): 
    productos=Productos.objects.all()
    categorias=Categorias.objects.all()    
    return render(request, "index.html",{"categorias":categorias,"productos":productos})

def producto(request,id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    return render(request,"producto.html",{"productos":producto})

def carrito(request,id_producto):
    carrito = Productos.objects.get(id_producto=id_producto)
    return render(request,"carrito.html",{"productos":carrito})

#añadir productos al carrito
#eliminar productos al carrito
#funcion de las categorias
# USUARIOS: registro y login (añadir usuarios, entrar a una cuenta)
# PRODUCTOS: añadir imagenes 



