from django.shortcuts import render, redirect, get_object_or_404
from .models import compras

def listarcompras(request):
    consultacompras = compras.objects.filter(estatus=True).order_by('-id')[:5]
    context = {'consultacompras': consultacompras, 'mostrar_todos': False}
    return render(request, 'compras/compras.html', context)

def listar_todas_compras(request):
    consultacompras = compras.objects.filter(estatus=True).order_by('-id')
    context = {'consultacompras': consultacompras, 'mostrar_todos': True}
    return render(request, 'compras/compras.html', context)

def crearcompra(request):
    if request.method == 'POST':
        compras.objects.create(
            folio=request.POST.get('folio', 'C-001'),
            fecha=request.POST['fecha'],
            subtotal=request.POST['subtotal'],
            iva=request.POST['iva'],
            total=request.POST['total']
        )
    return redirect('/pagecompras/')

def desactivarcompra(request, id):
    compra = get_object_or_404(compras, id=id)
    compra.estatus = False
    compra.save()
    return redirect('/pagecompras/')

def editarcompra(request, id):
    compra = get_object_or_404(compras, id=id)
    if request.method == 'POST':
        compra.folio = request.POST['folio']
        compra.fecha = request.POST['fecha']
        compra.subtotal = request.POST['subtotal']
        compra.iva = request.POST['iva']
        compra.total = request.POST['total']
        compra.save()
        return redirect('/pagecompras/')
    return render(request, 'compras/editar_compra.html', {'compra': compra})

def consultarcompra(request, id):
    compra = get_object_or_404(compras, id=id)
    return render(request, 'compras/consultar_compra.html', {'compra': compra})