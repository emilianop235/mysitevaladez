from django.shortcuts import render, redirect, get_object_or_404
from .models import usuarios
from grupos.models import grupos  # Importación relacional

def listarusuarios(request):
    consultausuarios = usuarios.objects.filter(estatus=True).order_by('-id')[:5]
    grupos_activos = grupos.objects.filter(estatus=True)
    return render(request, 'usuarios/usuarios.html', {'consultausuarios': consultausuarios, 'grupos_lista': grupos_activos, 'mostrar_todos': False})

def listar_todos_usuarios(request):
    consultausuarios = usuarios.objects.filter(estatus=True).order_by('-id')
    grupos_activos = grupos.objects.filter(estatus=True)
    return render(request, 'usuarios/usuarios.html', {'consultausuarios': consultausuarios, 'grupos_lista': grupos_activos, 'mostrar_todos': True})

def crearusuario(request):
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo_id')
        grupo_obj = get_object_or_404(grupos, id=grupo_id) if grupo_id else None
        usuarios.objects.create(
            nombre=request.POST['nombre'],
            usuario=request.POST['usuario'],
            passwd=request.POST['passwd'],
            correo=request.POST['correo'],
            grupo=grupo_obj
        )
    return redirect('/pageusuarios/')

def desactivarusuario(request, id):
    user = get_object_or_404(usuarios, id=id)
    user.estatus = False
    user.save()
    return redirect('/pageusuarios/')

def editarusuario(request, id):
    user = get_object_or_404(usuarios, id=id)
    grupos_activos = grupos.objects.filter(estatus=True)
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo_id')
        user.nombre = request.POST['nombre']
        user.usuario = request.POST['usuario']
        user.passwd = request.POST['passwd']
        user.correo = request.POST['correo']
        user.grupo = get_object_or_404(grupos, id=grupo_id) if grupo_id else None
        user.save()
        return redirect('/pageusuarios/')
    return render(request, 'usuarios/editar_usuario.html', {'usuario_obj': user, 'grupos_lista': grupos_activos})

def consultarusuario(request, id):
    user = get_object_or_404(usuarios, id=id)
    return render(request, 'usuarios/consultar_usuario.html', {'usuario_obj': user})

def listar_inactivos(request):
    consultausuarios = usuarios.objects.filter(estatus=False).order_by('-id')
    return render(request, 'usuarios/inactivos.html', {'consultausuarios': consultausuarios})

def restaurarusuario(request, id):
    user = get_object_or_404(usuarios, id=id)
    user.estatus = True
    user.save()
    return redirect('/pageusuarios/')