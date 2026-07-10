from django.shortcuts import render, redirect, get_object_or_404
from .models import nomina
# Importamos la clase Empleado para poder seleccionarlo en el formulario
from empleados.models import Empleado

def listarnominas(request):
    consultanominas = nomina.objects.filter(estatus=True).order_by('-id')[:5]
    empleados_activos = Empleado.objects.filter(estatus=True)
    context = {'consultanominas': consultanominas, 'empleados': empleados_activos, 'mostrar_todos': False}
    return render(request, 'nomina/nominas.html', context)

def listar_todas_nominas(request):
    consultanominas = nomina.objects.filter(estatus=True).order_by('-id')
    empleados_activos = Empleado.objects.filter(estatus=True)
    context = {'consultanominas': consultanominas, 'empleados': empleados_activos, 'mostrar_todos': True}
    return render(request, 'nomina/nominas.html', context)

def crearnomina(request):
    if request.method == 'POST':
        # Obtenemos la instancia del empleado seleccionado
        empleado_seleccionado = get_object_or_404(Empleado, id=request.POST['empleado_id'])
        
        nomina.objects.create(
            numperiodo=request.POST['numperiodo'],
            fecha=request.POST['fecha'],
            salario=request.POST['salario'],
            perceciones=request.POST['perceciones'],
            deducciones=request.POST['deducciones'],
            total=request.POST['total'],
            empleado=empleado_seleccionado
        )
    return redirect('/pagenomina/')

def desactivarnomina(request, id):
    registro_nomina = get_object_or_404(nomina, id=id)
    registro_nomina.estatus = False
    registro_nomina.save()
    return redirect('/pagenomina/')

def editarnomina(request, id):
    registro_nomina = get_object_or_404(nomina, id=id)
    empleados_activos = Empleado.objects.filter(estatus=True)
    
    if request.method == 'POST':
        empleado_seleccionado = get_object_or_404(Empleado, id=request.POST['empleado_id'])
        
        registro_nomina.numperiodo = request.POST['numperiodo']
        registro_nomina.fecha = request.POST['fecha']
        registro_nomina.salario = request.POST['salario']
        registro_nomina.perceciones = request.POST['perceciones']
        registro_nomina.deducciones = request.POST['deducciones']
        registro_nomina.total = request.POST['total']
        registro_nomina.empleado = empleado_seleccionado
        registro_nomina.save()
        return redirect('/pagenomina/')
        
    return render(request, 'nomina/editar_nomina.html', {
        'nomina': registro_nomina, 
        'empleados': empleados_activos
    })

def consultarnomina(request, id):
    registro_nomina = get_object_or_404(nomina, id=id)
    return render(request, 'nomina/consultar_nomina.html', {'nomina': registro_nomina})