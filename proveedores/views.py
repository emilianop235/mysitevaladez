from django.shortcuts import render, redirect, get_object_or_404
from .models import proveedores

def listarproveedores(request):
    consultaproveedores = proveedores.objects.filter(estatus=True).order_by('-id')[:5]
    context = {'consultaproveedores': consultaproveedores, 'mostrar_todos': False}
    return render(request, 'proveedores/proveedores.html', context)

def listar_todos_proveedores(request):
    consultaproveedores = proveedores.objects.filter(estatus=True).order_by('-id')
    context = {'consultaproveedores': consultaproveedores, 'mostrar_todos': True}
    return render(request, 'proveedores/proveedores.html', context)

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
    proveedor = get_object_or_404(proveedores, id=id)
    proveedor.estatus = False
    proveedor.save()
    return redirect('/pageproveedores/')

def editarproveedor(request, id):
    proveedor = get_object_or_404(proveedores, id=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.apellido = request.POST['apellido']
        proveedor.direccion = request.POST['direccion']
        proveedor.telefono = request.POST['telefono']
        proveedor.save()
        return redirect('/pageproveedores/')
    return render(request, 'proveedores/editar_proveedor.html', {'proveedor': proveedor})

def consultarproveedor(request, id):
    proveedor = get_object_or_404(proveedores, id=id)
    return render(request, 'proveedores/consultar_proveedor.html', {'proveedor': proveedor})