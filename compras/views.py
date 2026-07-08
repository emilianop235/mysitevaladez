from django.shortcuts import render, redirect
from .models import compra

def listarcompras(request):
    # Traemos las compras de la base de datos, ordenadas de la más reciente a la más antigua
    consultacompras = compra.objects.all().order_by('-fecha_compra')
    return render(request, 'compras/compras.html', {'consultacompras': consultacompras})

def crearcompra(request):
    if request.method == 'POST':
        compra.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            cantidad=request.POST['cantidad']
        )
    return redirect('/pagecompras/')