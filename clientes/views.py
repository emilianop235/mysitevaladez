from django.shortcuts import redirect, render
from .models import Cliente  # <-- Importamos Cliente con mayúscula

# 1. Función para mostrar la página y los datos de la tabla
def listaclientes(request): 
    # Usamos Cliente.objects.all()
    consultaclientes = Cliente.objects.all() 
    return render(request, 'clientes/clientes.html', {'consultaclientes': consultaclientes}) 

# 2. Función para guardar los datos
def crearclientes(request):
    # Creamos el objeto usando Cliente(...)
    nvocliente = Cliente(
        nombre = request.POST['nombre'],
        apellido = request.POST['apellido'],
        sexo = request.POST['sexo'],
        tipo = request.POST['tipo'],
        direccion = request.POST['direccion']
    )
    nvocliente.save() 
    return redirect('/pageclientes/')