from django.shortcuts import render, redirect
from .models import inventarios

def listar_inventarios(request):
    # Consultamos las existencias en inventario ordenadas por las más recientes
    consultainventarios = inventarios.objects.all().order_by('-id')
    return render(request, 'inventarios/inventarios.html', {'consultainventarios': consultainventarios})

def crear_inventario(request):
    if request.method == 'POST':
        inventarios.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            cantidad=request.POST['cantidad']
        )
    return redirect('/pageinventarios/')