from django.shortcuts import render, redirect
from .models import usuario

def validar_login(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        pwd = request.POST.get('contraseña')
        
        # Filtramos en la base de datos para ver si coinciden
        user = usuario.objects.filter(correo=email, contraseña=pwd).first()
        
        if user:
            return redirect('/pageclientes/') # Si existe, lo mandamos al CRM
        else:
            return render(request, 'usuarios/login.html', {'error': 'Datos incorrectos'})
    
    return render(request, 'usuarios/login.html')