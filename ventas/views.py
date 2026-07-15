from django.shortcuts import render, redirect, get_object_or_404
from .models import ventas
from clientes.models import Cliente
from productos.models import producto

def listarventas(request):
    consultaventas = ventas.objects.filter(estatus=True).order_by('-id')[:5]
    clientes_lista = Cliente.objects.filter(estatus=True)
    productos_lista = producto.objects.filter(estatus=True)
    return render(request, 'ventas/ventas.html', {
        'consultaventas': consultaventas,
        'clientes_lista': clientes_lista,
        'productos_lista': productos_lista,
        'mostrar_todos': False
    })

def listar_todas_ventas(request):
    consultaventas = ventas.objects.filter(estatus=True).order_by('-id')
    clientes_lista = Cliente.objects.filter(estatus=True)
    productos_lista = producto.objects.filter(estatus=True)
    return render(request, 'ventas/ventas.html', {
        'consultaventas': consultaventas,
        'clientes_lista': clientes_lista,
        'productos_lista': productos_lista,
        'mostrar_todos': True
    })

def crearventa(request):
    if request.method == 'POST':
        nueva_venta = ventas.objects.create(
            folio=request.POST.get('folio'),
            total=request.POST.get('total')
        )
        nueva_venta.clientes.set(request.POST.getlist('clientes_seleccionados'))
        nueva_venta.productos.set(request.POST.getlist('productos_seleccionados'))
        return redirect('/pageventas/')

def desactivarventa(request, id):
    venta = get_object_or_404(ventas, id=id)
    venta.estatus = False
    venta.save()
    return redirect('/pageventas/')

def editarventa(request, id):
    venta = get_object_or_404(ventas, id=id)
    if request.method == 'POST':
        venta.folio = request.POST.get('folio')
        venta.total = request.POST.get('total')
        venta.save()
        venta.clientes.set(request.POST.getlist('clientes_seleccionados'))
        venta.productos.set(request.POST.getlist('productos_seleccionados'))
        return redirect('/pageventas/')
        
    return render(request, 'ventas/editar_venta.html', {
        'venta': venta,
        'clientes_lista': Cliente.objects.filter(estatus=True),
        'productos_lista': producto.objects.filter(estatus=True)
    })

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