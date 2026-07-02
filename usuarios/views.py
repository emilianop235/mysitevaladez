from django.shortcuts import render, redirect
from .models import usuario

# Además de tu función de validar_login, pon estas dos:

from django.shortcuts import render, redirect
from .models import usuario  # Importamos tu clase del modelo para poder consultar PostgreSQL

# 1. Función para la pantalla de Login (Independiente, sin barra lateral)
def validar_login(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        pwd = request.POST.get('contraseña')
        
        # Filtramos en PostgreSQL para ver si el correo y la contraseña coinciden
        user = usuario.objects.filter(correo=email, contraseña=pwd).first()
        
        if user:
            return redirect('/pageclientes/')  # Si es correcto, lo deja pasar al CRM
        else:
            # Si falla, recarga el login mandando un mensaje de error
            return render(request, 'usuarios/login.html', {'error': 'Usuario o contraseña incorrectos'})
    
    return render(request, 'usuarios/login.html')

# 2. Función para la pantalla de Gestión (Con la tabla y barra lateral)
def listar_usuarios(request):
    consultausuarios = usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'consultausuarios': consultausuarios})

# 3. Función para registrar nuevos usuarios desde el panel
def crear_usuario(request):
    if request.method == 'POST':
        usuario.objects.create(
            usuario=request.POST['usuario'],
            correo=request.POST['correo'],
            contraseña=request.POST['contraseña']
        )
    return redirect('/pageusuarios/')