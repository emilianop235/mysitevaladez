from django.shortcuts import render, redirect, get_object_or_404
from .models import inventarios
from productos.models import producto 

def listarinventarios(request):
    consultainventarios = inventarios.objects.filter(estatus=True).order_by('-id')[:5]
    return render(request, 'inventarios/inventarios.html', {'consultainventarios': consultainventarios, 'mostrar_todos': False})

def listar_todos_inventarios(request):
    consultainventarios = inventarios.objects.filter(estatus=True).order_by('-id')
    return render(request, 'inventarios/inventarios.html', {'consultainventarios': consultainventarios, 'mostrar_todos': True})

def crearinventario(request):
    if request.method == 'POST':
        # Obtenemos el ID del producto que el usuario seleccionó en el HTML
        prod_id = request.POST.get('producto_id')
        prod_obj = get_object_or_404(producto, id=prod_id)
        
        inventarios.objects.create(
            producto=prod_obj, # Vinculamos el producto
            cantidad=request.POST.get('cantidad'),
            ubicacion=request.POST.get('ubicacion')
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
    # Pasamos los productos por si el usuario quiere cambiar qué producto es (opcional)
    return render(request, 'inventarios/editar_inventario.html', {
        'inventario': inv,
        'productos_lista': producto.objects.filter(estatus=True)
    })

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