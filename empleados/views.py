from django.shortcuts import render, redirect
from .models import Empleado

def listarempleados(request):
    consultarempleados = Empleado.objects.all()
    return render(request, 'empleado/empleados.html', {'consultarempleados': consultarempleados})

def crearempleado(request):
    Empleado.objects.create(
        nombre=request.POST['nombre'],
        apellido=request.POST['apellido'],
        sexo=request.POST['sexo'],
        tipo=request.POST['tipo']
    )
    return redirect('/pageempleados/')