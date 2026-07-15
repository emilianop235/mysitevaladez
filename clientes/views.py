from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

def listarclientes(request):
    consultaclientes = Cliente.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'clientes/clientes.html', {'consultaclientes': consultaclientes, 'mostrar_todos': False})

def listar_todos_clientes(request):
    consultaclientes = Cliente.objects.filter(estatus=True).order_by('-id')
    return render(request, 'clientes/clientes.html', {'consultaclientes': consultaclientes, 'mostrar_todos': True})

def crearcliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            sexo=request.POST['sexo'],
            tipo=request.POST['tipo'],
            direccion=request.POST['direccion']
        )
    return redirect('/pageclientes/')

def desactivarcliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.estatus = False
    cliente.save()
    return redirect('/pageclientes/')

def editarcliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.sexo = request.POST['sexo']
        cliente.tipo = request.POST['tipo']
        cliente.direccion = request.POST['direccion']
        cliente.save()
        return redirect('/pageclientes/')
    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})

def consultarcliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/consultar_cliente.html', {'cliente': cliente})

def listar_inactivos(request):
    consultaclientes = Cliente.objects.filter(estatus=False).order_by('-id')
    return render(request, 'clientes/inactivos.html', {'consultaclientes': consultaclientes})

def restaurarcliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.estatus = True
    cliente.save()
    return redirect('/pageclientes/')