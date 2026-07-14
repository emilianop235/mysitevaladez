from django.shortcuts import render, redirect, get_object_or_404
from .models import inventarios

def listarinventarios(request):
    consultainventarios = inventarios.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'inventarios/inventarios.html', {'consultainventarios': consultainventarios, 'mostrar_todos': False})

def listar_todos_inventarios(request):
    consultainventarios = inventarios.objects.filter(estatus=True).order_by('-id')
    return render(request, 'inventarios/inventarios.html', {'consultainventarios': consultainventarios, 'mostrar_todos': True})

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
    inv = get_object_or_404(inventarios, id=id)
    inv.estatus = False
    inv.save()
    return redirect('/pageinventarios/')

def editarinventario(request, id):
    inv = get_object_or_404(inventarios, id=id)
    if request.method == 'POST':
        inv.nombre = request.POST['nombre']
        inv.descripcion = request.POST['descripcion']
        inv.precio = request.POST['precio']
        inv.cantidad = request.POST['cantidad']
        inv.save()
        return redirect('/pageinventarios/')
    return render(request, 'inventarios/editar_inventario.html', {'inventario': inv})

def consultarinventario(request, id):
    inv = get_object_or_404(inventarios, id=id)
    return render(request, 'inventarios/consultar_inventario.html', {'inventario': inv})