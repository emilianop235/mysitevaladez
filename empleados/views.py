from django.shortcuts import render, redirect
from .models import Empleado

def listarempleados(request):
    consultarempleados = Empleado.objects.all()
    # Cambiamos la ruta a 'empleados/empleados.html' para que coincida con tu carpeta
    return render(request, 'empleados/empleados.html', {'consultarempleados': consultarempleados})

def crearempleado(request):
    Empleado.objects.create(
        nombre=request.POST['nombre'],
        apellido=request.POST['apellido'],
        sexo=request.POST['sexo'],
        tipo=request.POST['tipo']
    )
    return redirect('/pageempleados/')