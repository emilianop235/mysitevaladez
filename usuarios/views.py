from django.shortcuts import render, redirect, get_object_or_404
from .models import usuarios
from grupos.models import grupos  # Importamos para el Select del formulario

def listarusuarios(request):
    consultausuarios = usuarios.objects.filter(estatus=True).order_by('-id')[:5]
    grupos_activos = grupos.objects.filter(estatus=True)
    context = {'consultausuarios': consultausuarios, 'grupos_lista': grupos_activos, 'mostrar_todos': False}
    return render(request, 'usuarios/usuarios.html', context)

def listar_todos_usuarios(request):
    consultausuarios = usuarios.objects.filter(estatus=True).order_by('-id')
    grupos_activos = grupos.objects.filter(estatus=True)
    context = {'consultausuarios': consultausuarios, 'grupos_lista': grupos_activos, 'mostrar_todos': True}
    return render(request, 'usuarios/usuarios.html', context)

def crearusuario(request):
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo_id')
        grupo_seleccionado = get_object_or_404(grupos, id=grupo_id) if grupo_id else None
        
        usuarios.objects.create(
            nombre=request.POST['nombre'],
            usuario=request.POST['usuario'],
            passwd=request.POST['passwd'],
            correo=request.POST['correo'],
            grupo=grupo_seleccionado
        )
    return redirect('/pageusuarios/')

def desactivarusuario(request, id):
    item_usuario = get_object_or_404(usuarios, id=id)
    item_usuario.estatus = False
    item_usuario.save()
    return redirect('/pageusuarios/')

def editarusuario(request, id):
    item_usuario = get_object_or_404(usuarios, id=id)
    grupos_activos = grupos.objects.filter(estatus=True)
    
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo_id')
        grupo_seleccionado = get_object_or_404(grupos, id=grupo_id) if grupo_id else None
        
        item_usuario.nombre = request.POST['nombre']
        item_usuario.usuario = request.POST['usuario']
        item_usuario.passwd = request.POST['passwd']
        item_usuario.correo = request.POST['correo']
        item_usuario.grupo = grupo_seleccionado
        item_usuario.save()
        return redirect('/pageusuarios/')
        
    return render(request, 'usuarios/editar_usuario.html', {
        'usuario_obj': item_usuario, 
        'grupos_lista': grupos_activos
    })

def consultarusuario(request, id):
    item_usuario = get_object_or_404(usuarios, id=id)
    return render(request, 'usuarios/consultar_usuario.html', {'usuario_obj': item_usuario})