from django.shortcuts import render, redirect
from .models import sucursal

def listarsucursales(request):
    # Consultamos todas las sucursales dadas de alta
    consultasucursales = sucursal.objects.all().order_by('nombre')
    return render(request, 'sucursal/sucursal.html', {'consultasucursales': consultasucursales})

def crearsucursal(request):
    if request.method == 'POST':
        sucursal.objects.create(
            nombre=request.POST['nombre'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            encargado=request.POST['encargado']
        )
    return redirect('/pagesucursal/')