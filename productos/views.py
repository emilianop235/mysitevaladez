from django.shortcuts import render, redirect, get_object_or_404
from .models import producto

def listarproductos(request):
    consultaproductos = producto.objects.filter(estatus=True).order_by('-id')[:5]
    context = {'consultaproductos': consultaproductos, 'mostrar_todos': False}
    return render(request, 'productos/productos.html', context)

def listar_todos_productos(request):
    consultaproductos = producto.objects.filter(estatus=True).order_by('-id')
    context = {'consultaproductos': consultaproductos, 'mostrar_todos': True}
    return render(request, 'productos/productos.html', context)

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
    item_producto = get_object_or_404(producto, id=id)
    item_producto.estatus = False
    item_producto.save()
    return redirect('/pageproductos/')

def editarproducto(request, id):
    item_producto = get_object_or_404(producto, id=id)
    if request.method == 'POST':
        item_producto.nombre = request.POST['nombre']
        item_producto.descripcion = request.POST['descripcion']
        item_producto.precio = request.POST['precio']
        item_producto.stock = request.POST['stock']
        item_producto.save()
        return redirect('/pageproductos/')
    return render(request, 'productos/editar_producto.html', {'producto': item_producto})

def consultarproducto(request, id):
    item_producto = get_object_or_404(producto, id=id)
    return render(request, 'productos/consultar_producto.html', {'producto': item_producto})