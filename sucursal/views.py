from django.shortcuts import render, redirect, get_object_or_404
from .models import sucursal

def listarsucursales(request):
    consultasucursales = sucursal.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'sucursal/sucursales.html', {'consultasucursales': consultasucursales, 'mostrar_todos': False})

def listar_todas_sucursales(request):
    consultasucursales = sucursal.objects.filter(estatus=True).order_by('-id')
    return render(request, 'sucursal/sucursales.html', {'consultasucursales': consultasucursales, 'mostrar_todos': True})

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
    suc = get_object_or_404(sucursal, id=id)
    suc.estatus = False
    suc.save()
    return redirect('/pagesucursal/')

def editarsucursal(request, id):
    suc = get_object_or_404(sucursal, id=id)
    if request.method == 'POST':
        suc.nombre = request.POST['nombre']
        suc.direccion = request.POST['direccion']
        suc.telefono = request.POST['telefono']
        suc.encargado = request.POST['encargado']
        suc.save()
        return redirect('/pagesucursal/')
    return render(request, 'sucursal/editar_sucursal.html', {'sucursal': suc})

def consultarsucursal(request, id):
    suc = get_object_or_404(sucursal, id=id)
    return render(request, 'sucursal/consultar_sucursal.html', {'sucursal': suc})