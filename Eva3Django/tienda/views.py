from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from Eva3Django.forms import ProductoForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def index(request):
    if request.method=='GET':
      return render(request,"./index.html", {'form': AuthenticationForm})
    else:
        name = request.POST["username"]    
        password = request.POST["password"]
        user = authenticate(username=name,password=password)
        if user is None:
           return render(request,"./index.html", {'form': AuthenticationForm, 'error':"Usuario y/o Password incorrecto"})
        else: 
            return redirect("productos")

def productos(request):
    productos = Producto.objects.all()
    return render(request,"productos.html", {'productos': productos})

def nosotros(request):
    return render(request,"nosotros.html")

def sucursales(request):
    return render(request,"sucursales.html")

def contacto(request):
    return render(request,"contacto.html")

def gracias(request):
    return render(request,"gracias.html")

def crearProducto(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request,"crear.html", {'formulario': formulario})

def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'editar.html', {'formulario': formulario})

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')

def registro(request):
    if request.method=='GET':
       return render(request,"registro.html", {'form' : UserCreationForm})
    else: 
       if request.POST["password1"]!=request.POST["password2"]:
          return render(request,"registro.html", {'form' : UserCreationForm, 'error' : "Las contraseñas no coinciden" })
       else:
        name = request.POST["username"]    
        password = request.POST["password1"]
        user = User.objects.create_user(username=name,password=password)
        user.save()
    return render(request,"registro.html", {'form' : UserCreationForm, 'error' : "Usuario Registrado" })



