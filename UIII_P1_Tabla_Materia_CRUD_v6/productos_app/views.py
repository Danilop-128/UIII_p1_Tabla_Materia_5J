from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.

def inicio_vista(request):
    losproductos=Producto.objects.all()
    return render(request,"gestionarProductos.html",{"misproductos":losproductos})

def registrarProducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guardarProducto=Producto.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
    )#GUARDA EL REGISTRO

    return redirect("/")

def seleccionarProducto(request,codigo):
    producto=Producto.objects.get(codigo=codigo)
    return render(request,"editarproducto.html",{"misproductos":producto})




def editarProducto(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    producto=Producto.objects.get(codigo=codigo)
    producto.nombre=nombre
    producto.creditos=creditos
    producto.save() # guarda registro actualizado
    return redirect("/")



def borrarProducto(request,codigo):
    producto=Producto.objects.get(codigo=codigo)
    producto.delete() # borra el registro
    return redirect("/")


