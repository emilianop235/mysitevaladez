from django.shortcuts import render, redirect, get_object_or_404
from .models import producto

def listarproductos(request):
    consultaproductos = producto.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'productos/productos.html', {'consultaproductos': consultaproductos, 'mostrar_todos': False})

def listar_todos_productos(request):
    consultaproductos = producto.objects.filter(estatus=True).order_by('-id')
    return render(request, 'productos/productos.html', {'consultaproductos': consultaproductos, 'mostrar_todos': True})

def crearproducto(request):
    if request.method == 'POST':
        producto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            stock=request.POST['stock']
        )
    return redirect('/pageproductos/')

def desactivarproducto(request, id):
    prod = get_object_or_404(producto, id=id)
    prod.estatus = False
    prod.save()
    return redirect('/pageproductos/')

def editarproducto(request, id):
    prod = get_object_or_404(producto, id=id)
    if request.method == 'POST':
        prod.nombre = request.POST['nombre']
        prod.descripcion = request.POST['descripcion']
        prod.precio = request.POST['precio']
        prod.stock = request.POST['stock']
        prod.save()
        return redirect('/pageproductos/')
    return render(request, 'productos/editar_producto.html', {'producto': prod})

def consultarproducto(request, id):
    prod = get_object_or_404(producto, id=id)
    return render(request, 'productos/consultar_producto.html', {'producto': prod})

def listar_inactivos(request):
    consultaproductos = producto.objects.filter(estatus=False).order_by('-id')
    return render(request, 'productos/inactivos.html', {'consultaproductos': consultaproductos})

def restaurarproducto(request, id):
    prod = get_object_or_404(producto, id=id)
    prod.estatus = True
    prod.save()
    return redirect('/pageproductos/')