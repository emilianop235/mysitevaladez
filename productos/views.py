from django.shortcuts import render
from django.http import HttpResponse

def productos(request):
    #return HttpResponse("Formularios de productos-emiliano")
    return render(request, 'productos/productos.html')
