from django.shortcuts import render, redirect, get_object_or_404
from .models import proveedores

def listarproveedores(request):
    consultaproveedores = proveedores.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'proveedores/proveedores.html', {'consultaproveedores': consultaproveedores, 'mostrar_todos': False})

def listar_todos_proveedores(request):
    consultaproveedores = proveedores.objects.filter(estatus=True).order_by('-id')
    return render(request, 'proveedores/proveedores.html', {'consultaproveedores': consultaproveedores, 'mostrar_todos': True})

def crearproveedor(request):
    if request.method == 'POST':
        proveedores.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono']
        )
    return redirect('/pageproveedores/')

def desactivarproveedor(request, id):
    prov = get_object_or_404(proveedores, id=id)
    prov.estatus = False
    prov.save()
    return redirect('/pageproveedores/')

def editarproveedor(request, id):
    prov = get_object_or_404(proveedores, id=id)
    if request.method == 'POST':
        prov.nombre = request.POST['nombre']
        prov.apellido = request.POST['apellido']
        prov.direccion = request.POST['direccion']
        prov.telefono = request.POST['telefono']
        prov.save()
        return redirect('/pageproveedores/')
    return render(request, 'proveedores/editar_proveedor.html', {'proveedor': prov})

def consultarproveedor(request, id):
    prov = get_object_or_404(proveedores, id=id)
    return render(request, 'proveedores/consultar_proveedor.html', {'proveedor': prov})

def listar_inactivos(request):
    consultaproveedores = proveedores.objects.filter(estatus=False).order_by('-id')
    return render(request, 'proveedores/inactivos.html', {'consultaproveedores': consultaproveedores})

def restaurarproveedor(request, id):
    prov = get_object_or_404(proveedores, id=id)
    prov.estatus = True
    prov.save()
    return redirect('/pageproveedores/')