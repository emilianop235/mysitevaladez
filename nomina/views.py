from django.shortcuts import render, redirect
from .models import Empleado, nomina 

def listarnominas(request):
    consultanominas = nomina.objects.all().order_by('-fecha')
    consultaempleados = Empleado.objects.all() 
    
    context = {
        'consultanominas': consultanominas,
        'consultaempleados': consultaempleados
    }
    return render(request, 'nomina/nomina.html', context)

def crearnomina(request):
    if request.method == 'POST':
        nomina.objects.create(
            numperiodo=request.POST['numperiodo'],
            fecha=request.POST['fecha'],
            salario=request.POST['salario'],
            perceciones=request.POST['perceciones'], 
            deducciones=request.POST['deducciones'],
            total=request.POST['total'],
            empleado_id=request.POST['empleado'] 
        )
    return redirect('/pagenomina/')