from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
import Cliente
def listarclientes(request):
    consultaclientes = Cliente.objects.filter(estatus=True).order_by('-id')[:5]
    context = {'consultaclientes': consultaclientes, 'mostrar_todos': False}
    return render(request, 'clientes/clientes.html', context)

def listar_todos_clientes(request):
    consultaclientes = Cliente.objects.filter(estatus=True).order_by('-id')
    context = {'consultaclientes': consultaclientes, 'mostrar_todos': True}
    return render(request, 'clientes/clientes.html', context)

def crearcliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            telefono=request.POST['telefono']
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
        cliente.telefono = request.POST['telefono']
        cliente.save()
        return redirect('/pageclientes/')
    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})

def consultarcliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/consultar_cliente.html', {'cliente': cliente})