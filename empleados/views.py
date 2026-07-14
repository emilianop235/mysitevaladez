from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

def listarempleados(request):
    consultaempleados = Empleado.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'empleados/empleados.html', {'consultaempleados': consultaempleados, 'mostrar_todos': False})

def listar_todos_empleados(request):
    consultaempleados = Empleado.objects.filter(estatus=True).order_by('-id')
    return render(request, 'empleados/empleados.html', {'consultaempleados': consultaempleados, 'mostrar_todos': True})

def crearempleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            sexo=request.POST['sexo'],
            tipo=request.POST['tipo']
        )
    return redirect('/pageempleados/')

def desactivarempleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.estatus = False
    empleado.save()
    return redirect('/pageempleados/')

def editarempleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.sexo = request.POST['sexo']
        empleado.tipo = request.POST['tipo']
        empleado.save()
        return redirect('/pageempleados/')
    return render(request, 'empleados/editar_empleado.html', {'empleado': empleado})

def consultarempleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'empleados/consultar_empleado.html', {'empleado': empleado})