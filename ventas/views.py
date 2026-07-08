from django.shortcuts import render, redirect
from .models import ventas
from clientes.models import Cliente
from empleados.models import Empleado
from productos.models import Producto

def listar_ventas(request):
    consultaventas = ventas.objects.all().order_by('-fecha')
    
    # Traemos todos los catálogos para llenar las opciones desplegables del formulario
    consultaclientes = Cliente.objects.all()
    consultaempleados = Empleado.objects.all()
    consultaproductos = Producto.objects.all()

    context = {
        'consultaventas': consultaventas,
        'consultaclientes': consultaclientes,
        'consultaempleados': consultaempleados,
        'consultaproductos': consultaproductos
    }
    return render(request, 'ventas/ventas.html', context)

def crear_venta(request):
    if request.method == 'POST':
        ventas.objects.create(
            cliente_id=request.POST['cliente'],
            empleado_id=request.POST['empleado'],
            producto_id=request.POST['producto'],
            cantidad=request.POST['cantidad'],
            total=request.POST['total']
        )
    return redirect('/pageventas/')