from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
    #return HttpResponse("Formularios de clientes-emiliano")
    return render(request, 'clientes/clientes.html')


