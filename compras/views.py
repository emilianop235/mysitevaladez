from django.shortcuts import render, redirect, get_object_or_404
from .models import compras
from proveedores.models import proveedores
from productos.models import producto

def listarcompras(request):
    consultacompras = compras.objects.filter(estatus=True).order_by('-id')[:5]
    prov_lista = proveedores.objects.filter(estatus=True)
    prod_lista = producto.objects.filter(estatus=True)
    return render(request, 'compras/compras.html', {
        'consultacompras': consultacompras,
        'proveedores_lista': prov_lista,
        'productos_lista': prod_lista,
        'mostrar_todos': False
    })

def listar_todas_compras(request):
    consultacompras = compras.objects.filter(estatus=True).order_by('-id')
    prov_lista = proveedores.objects.filter(estatus=True)
    prod_lista = producto.objects.filter(estatus=True)
    return render(request, 'compras/compras.html', {
        'consultacompras': consultacompras,
        'proveedores_lista': prov_lista,
        'productos_lista': prod_lista,
        'mostrar_todos': True
    })

def crearcompra(request):
    if request.method == 'POST':
        nueva_compra = compras.objects.create(
            folio=request.POST.get('folio'),
            subtotal=request.POST.get('subtotal'),
            iva=request.POST.get('iva'),
            total=request.POST.get('total')
        )
        nueva_compra.proveedores.set(request.POST.getlist('proveedores_seleccionados'))
        nueva_compra.productos.set(request.POST.getlist('productos_seleccionados'))
        return redirect('/pagecompras/')
    return redirect('/pagecompras/')

def desactivarcompra(request, id):
    comp = get_object_or_404(compras, id=id)
    comp.estatus = False
    comp.save()
    return redirect('/pagecompras/')

def editarcompra(request, id):
    compra = get_object_or_404(compras, id=id)
    if request.method == 'POST':
        compra.folio = request.POST.get('folio')
        compra.subtotal = request.POST.get('subtotal')
        compra.iva = request.POST.get('iva')
        compra.total = request.POST.get('total')
        compra.save()
        compra.proveedores.set(request.POST.getlist('proveedores_seleccionados'))
        compra.productos.set(request.POST.getlist('productos_seleccionados'))
        return redirect('/pagecompras/')
    
    return render(request, 'compras/editar_compra.html', {
        'compra': compra,
        'proveedores_lista': proveedores.objects.filter(estatus=True),
        'productos_lista': producto.objects.filter(estatus=True)
    })

def consultarcompra(request, id):
    return render(request, 'compras/consultar_compra.html', {'compra': get_object_or_404(compras, id=id)})

def listar_inactivos(request):
    consultacompras = compras.objects.filter(estatus=False).order_by('-id')
    return render(request, 'compras/inactivos.html', {'consultacompras': consultacompras})

def restaurarcompra(request, id):
    comp = get_object_or_404(compras, id=id)
    comp.estatus = True
    comp.save()
    return redirect('/pagecompras/')