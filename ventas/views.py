from django.shortcuts import render, redirect, get_object_or_404
from .models import ventas
from clientes.models import Cliente      # Importación relacional
from productos.models import producto    # Importación relacional

def listarventas(request):
    consultaventas = ventas.objects.filter(estatus=True).order_by('-id')[:5]
    cli_lista = Cliente.objects.filter(estatus=True)
    prod_lista = producto.objects.filter(estatus=True)
    return render(request, 'ventas/ventas.html', {
        'consultaventas': consultaventas,
        'clientes_lista': cli_lista,
        'productos_lista': prod_lista,
        'mostrar_todos': False
    })

def listar_todas_ventas(request):
    consultaventas = ventas.objects.filter(estatus=True).order_by('-id')
    cli_lista = Cliente.objects.filter(estatus=True)
    prod_lista = producto.objects.filter(estatus=True)
    return render(request, 'ventas/ventas.html', {
        'consultaventas': consultaventas,
        'clientes_lista': cli_lista,
        'productos_lista': prod_lista,
        'mostrar_todos': True
    })

def crearventa(request):
    if request.method == 'POST':
        nueva_venta = ventas.objects.create(
            folio=request.POST.get('folio', 'V-001'),
            total=request.POST.get('total', 0.0)
        )
        # Jalar relaciones vivas dinámicamente mediante arrays de IDs sin escribir a mano
        nueva_venta.cliente.set(request.POST.getlist('clientes_seleccionados'))
        nueva_venta.producto.set(request.POST.getlist('productos_seleccionados'))
    return redirect('/pageventas/')

def desactivarventa(request, id):
    venta = get_object_or_404(ventas, id=id)
    venta.estatus = False
    venta.save()
    return redirect('/pageventas/')

def editarventa(request, id):
    venta = get_object_or_404(ventas, id=id)
    if request.method == 'POST':
        venta.folio = request.POST.get('folio', venta.folio)
        venta.total = request.POST.get('total', venta.total)
        venta.cliente.set(request.POST.getlist('clientes_seleccionados'))
        venta.producto.set(request.POST.getlist('productos_seleccionados'))
        venta.save()
        return redirect('/pageventas/')
    return render(request, 'ventas/editar_venta.html', {'venta': venta})

def consultarventa(request, id):
    venta = get_object_or_404(ventas, id=id)
    return render(request, 'ventas/consultar_venta.html', {'venta': venta})

def listar_inactivos(request):
    consultaventas = ventas.objects.filter(estatus=False).order_by('-id')
    return render(request, 'ventas/inactivos.html', {'consultaventas': consultaventas})

def restaurarventa(request, id):
    venta = get_object_or_404(ventas, id=id)
    venta.estatus = True
    venta.save()
    return redirect('/pageventas/')