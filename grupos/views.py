from django.shortcuts import render, redirect
from .models import grupos

def listargrupos(request):
    # Consultamos todas las clasificaciones de la base de datos
    consultagrupos = grupos.objects.all().order_by('nombre')
    return render(request, 'grupos/grupos.html', {'consultagrupos': consultagrupos})

def creargrupo(request):
    if request.method == 'POST':
        # Para el estatus, revisamos si viene marcado desde el formulario
        estatus_form = request.POST.get('estatus') == 'on'
        
        grupos.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            estatus=estatus_form
        )
    return redirect('/pagegrupos/')