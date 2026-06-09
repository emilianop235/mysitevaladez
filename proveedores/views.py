from django.shortcuts import render
from django.http import HttpResponse

def proveedores(request):
    #return HttpResponse("Formularios de proveedores-emiliano")
    return render(request, 'proveedores/proveedores.html')
