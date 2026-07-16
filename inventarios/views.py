from django.shortcuts import render, redirect, get_object_or_404
from .models import inventarios
from productos.models import producto
from proveedores.models import proveedores as ModeloProveedor
from sucursal.models import sucursal as ModeloSucursal

def listarinventarios(request):
    consultainventarios = inventarios.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'inventarios/inventarios.html', {
        'consultainventarios': consultainventarios,
        'productos_lista': producto.objects.filter(estatus=True),      
        'proveedores_lista': ModeloProveedor.objects.filter(estatus=True), 
        'sucursales_lista': ModeloSucursal.objects.filter(estatus=True), # <-- Pasamos las sucursales
        'mostrar_todos': False
    })

def listar_todos_inventarios(request):
    consultainventarios = inventarios.objects.filter(estatus=True).order_by('-id')
    return render(request, 'inventarios/inventarios.html', {
        'consultainventarios': consultainventarios, 
        'productos_lista': producto.objects.filter(estatus=True),          
        'proveedores_lista': ModeloProveedor.objects.filter(estatus=True),
        'sucursales_lista': ModeloSucursal.objects.filter(estatus=True), # <-- Pasamos las sucursales
        'mostrar_todos': True
    })

def crearinventario(request):
    if request.method == 'POST':
        prod_id = request.POST.get('producto_id')
        prov_id = request.POST.get('proveedor_id')
        suc_id = request.POST.get('sucursal_id')
        
        prod_obj = get_object_or_404(producto, id=prod_id)
        prov_obj = get_object_or_404(ModeloProveedor, id=prov_id) if prov_id else None
        suc_obj = get_object_or_404(ModeloSucursal, id=suc_id) if suc_id else None # <-- Buscamos la sucursal

        inventarios.objects.create(
            nombre=prod_obj.nombre,
            descripcion=prod_obj.descripcion,
            precio=prod_obj.precio,
            cantidad=request.POST.get('cantidad', 1),
            
            producto_relacionado=prod_obj,
            proveedor=prov_obj,
            sucursal=suc_obj, # <-- La guardamos
            ubicacion=request.POST.get('ubicacion', 'Almacén General')
        )
    return redirect('/pageinventarios/')

def desactivarinventario(request, id):
    inv = get_object_or_404(inventarios, id=id)
    inv.estatus = False
    inv.save()
    return redirect('/pageinventarios/')

def editarinventario(request, id):
    inv = get_object_or_404(inventarios, id=id)
    if request.method == 'POST':
        inv.cantidad = request.POST.get('cantidad')
        inv.ubicacion = request.POST.get('ubicacion')
        inv.save()
        return redirect('/pageinventarios/')
    return render(request, 'inventarios/editar_inventario.html', {'inventario': inv})

def consultarinventario(request, id):
    inv = get_object_or_404(inventarios, id=id)
    return render(request, 'inventarios/consultar_inventario.html', {'inventario': inv})

def listar_inactivos(request):
    consultainventarios = inventarios.objects.filter(estatus=False).order_by('-id')
    return render(request, 'inventarios/inactivos.html', {'consultainventarios': consultainventarios})

def restaurarinventario(request, id):
    inv = get_object_or_404(inventarios, id=id)
    inv.estatus = True
    inv.save()
    return redirect('/pageinventarios/')