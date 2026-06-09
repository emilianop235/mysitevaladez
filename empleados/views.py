from django.shortcuts import render
from django.http import HttpResponse

def empleados(request):
    #return HttpResponse("Formularios de empleados-emiliano")
    return render(request, 'empleados/empleados.html')
