from django.shortcuts import render, redirect
# Importamos la clase 'ventas' (en minúscula) de este módulo
from .models import ventas

# Importamos las clases en minúscula de tus otras carpetas
from clientes.models import Cliente
from empleados.models import Empleado
from productos.models import producto

def listar_ventas(request):
    # Traemos el historial de la clase 'ventas' ordenado por fecha
    consultaventas = ventas.objects.all().order_by('-fecha')
    
    # Traemos todos los catálogos en minúsculas para las listas desplegables
    consultaclientes = Cliente.objects.all()
    consultaempleados = Empleado.objects.all()
    consultaproductos = producto.objects.all()

    # Empaquetamos todo para enviarlo al archivo HTML
    context = {
        'consultaventas': consultaventas,
        'consultaclientes': consultaclientes,
        'consultaempleados': consultaempleados,
        'consultaproductos': consultaproductos
    }
    return render(request, 'ventas/ventas.html', context)

def crear_venta(request):
    if request.method == 'POST':
        # Guardamos el registro usando la clase 'ventas'
        ventas.objects.create(
            cliente_id=request.POST['cliente'],
            empleado_id=request.POST['empleado'],
            producto_id=request.POST['producto'],
            cantidad=request.POST['cantidad'],
            total=request.POST['total']
        )
    return redirect('/pageventas/')