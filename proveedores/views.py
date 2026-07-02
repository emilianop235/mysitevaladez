from django.shortcuts import render, redirect
from .models import proveedores

def listarproveedores(request):
    consultaproveedores = proveedores.objects.all()
    return render(request, 'proveedores/proveedores.html', {'consultaproveedores': consultaproveedores})

def crearproveedor(request):
    if request.method == 'POST':
        proveedores.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono']
        )
    return redirect('/pageproveedores/')