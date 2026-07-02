from django.shortcuts import render, redirect
from .models import producto

def listarproductos(request):
    consultaproductos = producto.objects.all()
    return render(request, 'productos/productos.html', {'consultaproductos': consultaproductos})

def crearproducto(request):
    producto.objects.create(
        nombre=request.POST['nombre'],
        descripcion=request.POST['descripcion'],
        precio=request.POST['precio'],
        stock=request.POST['stock']
    )
    return redirect('/pageproductos/')