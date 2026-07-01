from django.shortcuts import redirect, render
from django.http import HttpResponse

def clientes(request):
    return render(request, 'clientes/clientes.html')

def crearclientes(request):
    nvocliente = clientes(
        nombre = request.POST['nombre'],
        apellido = request.POST['apellido'],
        sexo = request.POST['sexo'],
        tipo = request.POST['tipo'],
        direccion = request.POST['direccion']
    )
    nvocliente.save()
    return redirect('pageclientes')
