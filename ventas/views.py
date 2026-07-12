from django.shortcuts import render, redirect, get_object_or_404
from .models import ventas

def listarventas(request):
    consultaventas = ventas.objects.filter(estatus=True).order_by('-id')[:5]
    context = {'consultaventas': consultaventas, 'mostrar_todos': False}
    return render(request, 'ventas/ventas.html', context)

def listar_todas_ventas(request):
    consultaventas = ventas.objects.filter(estatus=True).order_by('-id')
    context = {'consultaventas': consultaventas, 'mostrar_todos': True}
    return render(request, 'ventas/ventas.html', context)

def crearventa(request):
    if request.method == 'POST':
        ventas.objects.create(
            folio=request.POST.get('folio', 'V-001'),
            total=request.POST.get('total', 0.0)
        )
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
        venta.save()
        return redirect('/pageventas/')
    return render(request, 'ventas/editar_venta.html', {'venta': venta})

def consultarventa(request, id):
    venta = get_object_or_404(ventas, id=id)
    return render(request, 'ventas/consultar_venta.html', {'venta': venta})