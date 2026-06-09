from django.shortcuts import render
from django.http import HttpResponse

def usuarios(request):
    #return HttpResponse("Formularios de usuarios-emiliano")
    return render(request, 'usuarios/usuarios.html')
