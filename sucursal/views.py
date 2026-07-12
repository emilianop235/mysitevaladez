from django.shortcuts import render, redirect, get_object_or_404
from .models import sucursal

def listarsucursales(request):
    consultasucursales = sucursal.objects.filter(estatus=True).order_by('-id')[:5]
    context = {'consultasucursales': consultasucursales, 'mostrar_todos': False}
    return render(request, 'sucursal/sucursales.html', context)

def listar_todas_sucursales(request):
    consultasucursales = sucursal.objects.filter(estatus=True).order_by('-id')
    context = {'consultasucursales': consultasucursales, 'mostrar_todos': True}
    return render(request, 'sucursal/sucursales.html', context)

def crearsucursal(request):
    if request.method == 'POST':
        sucursal.objects.create(
            nombre=request.POST['nombre'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            encargado=request.POST.get('encargado', 'Por asignar')
        )
    return redirect('/pagesucursal/')

def desactivarsucursal(request, id):
    item_sucursal = get_object_or_404(sucursal, id=id)
    item_sucursal.estatus = False
    item_sucursal.save()
    return redirect('/pagesucursal/')

def editarsucursal(request, id):
    item_sucursal = get_object_or_404(sucursal, id=id)
    if request.method == 'POST':
        item_sucursal.nombre = request.POST['nombre']
        item_sucursal.direccion = request.POST['direccion']
        item_sucursal.telefono = request.POST['telefono']
        item_sucursal.encargado = request.POST['encargado']
        item_sucursal.save()
        return redirect('/pagesucursal/')
    return render(request, 'sucursal/editar_sucursal.html', {'sucursal': item_sucursal})

def consultarsucursal(request, id):
    item_sucursal = get_object_or_404(sucursal, id=id)
    return render(request, 'sucursal/consultar_sucursal.html', {'sucursal': item_sucursal})