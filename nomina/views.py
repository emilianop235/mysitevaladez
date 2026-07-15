from django.shortcuts import render, redirect, get_object_or_404
from .models import nomina
from empleados.models import Empleado  # Importación relacional

def listarnominas(request):
    consultanominas = nomina.objects.filter(estatus=True).order_by('-id')[:5]
    emp_lista = Empleado.objects.filter(estatus=True)
    return render(request, 'nomina/nominas.html', {'consultanominas': consultanominas, 'empleados': emp_lista, 'mostrar_todos': False})

def listar_todas_nominas(request):
    consultanominas = nomina.objects.filter(estatus=True).order_by('-id')
    emp_lista = Empleado.objects.filter(estatus=True)
    return render(request, 'nomina/nominas.html', {'consultanominas': consultanominas, 'empleados': emp_lista, 'mostrar_todos': True})

def crearnomina(request):
    if request.method == 'POST':
        emp_obj = get_object_or_404(Empleado, id=request.POST['empleado_id'])
        nomina.objects.create(
            numperiodo=request.POST['numperiodo'],
            fecha=request.POST['fecha'],
            salario=request.POST['salario'],
            perceciones=request.POST['perceciones'],
            deducciones=request.POST['deducciones'],
            total=request.POST['total'],
            empleado=emp_obj
        )
    return redirect('/pagenomina/')

def desactivarnomina(request, id):
    nom = get_object_or_404(nomina, id=id)
    nom.estatus = False
    nom.save()
    return redirect('/pagenomina/')

def editarnomina(request, id):
    nom = get_object_or_404(nomina, id=id)
    emp_lista = Empleado.objects.filter(estatus=True)
    if request.method == 'POST':
        nom.numperiodo = request.POST['numperiodo']
        nom.fecha = request.POST['fecha']
        nom.salario = request.POST['salario']
        nom.perceciones = request.POST['perceciones']
        nom.deducciones = request.POST['deducciones']
        nom.total = request.POST['total']
        nom.empleado = get_object_or_404(Empleado, id=request.POST['empleado_id'])
        nom.save()
        return redirect('/pagenomina/')
    return render(request, 'nomina/editar_nomina.html', {'nomina': nom, 'empleados': emp_lista})

def consultarnomina(request, id):
    nom = get_object_or_404(nomina, id=id)
    return render(request, 'nomina/consultar_nomina.html', {'nomina': nom})

def listar_inactivos(request):
    consultanominas = nomina.objects.filter(estatus=False).order_by('-id')
    return render(request, 'nomina/inactivos.html', {'consultanominas': consultanominas})

def restaurarnomina(request, id):
    nom = get_object_or_404(nomina, id=id)
    nom.estatus = True
    nom.save()
    return redirect('/pagenomina/')