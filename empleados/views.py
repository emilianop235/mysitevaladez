from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

def pageempleados(request):
    consultaempleados = Empleado.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'empleados/empleados.html', {'consultaempleados': consultaempleados, 'mostrar_todos': False})

def pageempleados_todos(request):
    consultaempleados = Empleado.objects.filter(estatus=True).order_by('-id')
    return render(request, 'empleados/empleados.html', {'consultaempleados': consultaempleados, 'mostrar_todos': True})

def nuevo_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sexo = request.POST.get('sexo')
        tipo = request.POST.get('tipo')
        salario_base = request.POST.get('salario_base', 0.0)
        Empleado.objects.create(nombre=nombre, apellido=apellido, sexo=sexo, tipo=tipo, salario_base=salario_base)
    return redirect('/pageempleados/')

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.sexo = request.POST.get('sexo')
        empleado.tipo = request.POST.get('tipo')
        empleado.salario_base = request.POST.get('salario_base', 0.0)
        empleado.save()
        return redirect('/pageempleados/')
    return render(request, 'empleados/editar_empleado.html', {'empleado': empleado})

def consultar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'empleados/consultar_empleado.html', {'empleado': empleado})

def desactivar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.estatus = False
    empleado.save()
    return redirect('/pageempleados/')

def listar_inactivos(request):
    consultaempleados = Empleado.objects.filter(estatus=False).order_by('-id')
    return render(request, 'empleados/inactivos.html', {'consultaempleados': consultaempleados})

def restaurarempleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.estatus = True
    empleado.save()
    return redirect('/pageempleados/')