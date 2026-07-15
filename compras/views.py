from django.shortcuts import render, redirect, get_object_or_404
from .models import compras
from proveedores.models import proveedores  # Importación relacional
from productos.models import producto      # Importación relacional

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
            folio=request.POST.get('folio', 'C-001'),
            subtotal=request.POST.get('subtotal', 0.0),
            iva=request.POST.get('iva', 0.0),
            total=request.POST.get('total', 0.0)
        )
        # Jalar relaciones vivas dinámicamente mediante arrays de IDs sin escribir a mano
        nueva_compra.proveedor.set(request.POST.getlist('proveedores_seleccionados'))
        nueva_compra.producto.set(request.POST.getlist('productos_seleccionados'))
    return redirect('/pagecompras/')

def desactivarcompra(request, id):
    comp = get_object_or_404(compras, id=id)
    comp.estatus = False
    comp.save()
    return redirect('/pagecompras/')

# Asegúrate de tener importados los modelos arriba:
# from proveedores.models import Proveedor (o como se llame tu modelo)
# from productos.models import Producto

def editarcompra(request, id):
    compra = get_object_or_404(compras, id=id) # O como se llame tu modelo de compra
    
    if request.method == 'POST':
        # ... Aquí va tu lógica de guardado que ya tenías ...
        compra.folio = request.POST.get('folio')
        # ...
        compra.save()
        return redirect('/pagecompras/')
        
    # ESTO ES LO QUE FALTABA: Traer las listas para enviarlas al HTML
    proveedores_lista = proveedores.objects.filter(estatus=True) # Ajusta el nombre de tu modelo
    productos_lista = producto.objects.filter(estatus=True)      # Ajusta el nombre de tu modelo

    # Y aquí se las mandamos al diccionario de contexto:
    return render(request, 'compras/editar_compra.html', {
        'compra': compra,
        'proveedores_lista': proveedores_lista,
        'productos_lista': productos_lista
    })
def consultarcompra(request, id):
    comp = get_object_or_404(compras, id=id)
    return render(request, 'compras/consultar_compra.html', {'compra': comp})

def listar_inactivos(request):
    consultacompras = compras.objects.filter(estatus=False).order_by('-id')
    return render(request, 'compras/inactivos.html', {'consultacompras': consultacompras})

def restaurarcompra(request, id):
    comp = get_object_or_404(compras, id=id)
    comp.estatus = True
    comp.save()
    return redirect('/pagecompras/')