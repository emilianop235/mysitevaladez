from django.shortcuts import render, redirect, get_object_or_404
from .models import grupos

def listargrupos(request):
    consultagrupos = grupos.objects.filter(estatus=True).order_by('-id')[:5]
    context = {'consultagrupos': consultagrupos, 'mostrar_todos': False}
    return render(request, 'grupos/grupos.html', context)

def listar_todos_grupos(request):
    consultagrupos = grupos.objects.filter(estatus=True).order_by('-id')
    context = {'consultagrupos': consultagrupos, 'mostrar_todos': True}
    return render(request, 'grupos/grupos.html', context)

def creargrupo(request):
    if request.method == 'POST':
        grupos.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion']
            # fecha_creacion y estatus se ponen solos por defecto en el modelo
        )
    return redirect('/pagegrupos/')

def desactivargrupo(request, id):
    grupo = get_object_or_404(grupos, id=id)
    grupo.estatus = False
    grupo.save()
    return redirect('/pagegrupos/')

def editargrupo(request, id):
    grupo = get_object_or_404(grupos, id=id)
    if request.method == 'POST':
        grupo.nombre = request.POST['nombre']
        grupo.descripcion = request.POST['descripcion']
        grupo.save()
        return redirect('/pagegrupos/')
    return render(request, 'grupos/editar_grupo.html', {'grupo': grupo})

def consultargrupo(request, id):
    grupo = get_object_or_404(grupos, id=id)
    return render(request, 'grupos/consultar_grupo.html', {'grupo': grupo})