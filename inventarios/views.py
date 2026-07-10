from django.shortcuts import render, redirect, get_object_or_404
from .models import inventarios

def listarinventarios(request):
    consultainventarios = inventarios.objects.filter(estatus=True).order_by('-id')[:5]
    context = {'consultainventarios': consultainventarios, 'mostrar_todos': False}
    return render(request, 'inventarios/inventarios.html', context)

def listar_todos_inventarios(request):
    consultainventarios = inventarios.objects.filter(estatus=True).order_by('-id')
    context = {'consultainventarios': consultainventarios, 'mostrar_todos': True}
    return render(request, 'inventarios/inventarios.html', context)

def crearinventario(request):
    if request.method == 'POST':
        inventarios.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            cantidad=request.POST['cantidad']
        )
    return redirect('/pageinventarios/')

def desactivarinventario(request, id):
    inventario = get_object_or_404(inventarios, id=id)
    inventario.estatus = False
    inventario.save()
    return redirect('/pageinventarios/')

def editarinventario(request, id):
    inventario = get_object_or_404(inventarios, id=id)
    if request.method == 'POST':
        inventario.nombre = request.POST['nombre']
        inventario.descripcion = request.POST['descripcion']
        inventario.precio = request.POST['precio']
        inventario.cantidad = request.POST['cantidad']
        inventario.save()
        return redirect('/pageinventarios/')
    return render(request, 'inventarios/editar_inventario.html', {'inventario': inventario})

def consultarinventario(request, id):
    inventario = get_object_or_404(inventarios, id=id)
    return render(request, 'inventarios/consultar_inventario.html', {'inventario': inventario})