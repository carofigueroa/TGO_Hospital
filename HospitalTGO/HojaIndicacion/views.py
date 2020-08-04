from django.shortcuts import render

# Create your views here.
from HojaIndicacion.models import paciente, hoja_indicaciones, cirugias, medicamentos
import json
# Create your views here.

def main(request):
    return render(request,'main.html')

def cirugia(request):
    contador=[]
    cir_hoja=hoja_indicaciones.objects.values_list('Nombre_cirugias',flat=True)
    cir_pacientes=[i for i in cir_hoja]
    lista=[]
    ale=cirugias.objects.values_list('nombre_cirugia',flat=True)
    vale=[i for i in ale]
    contador=[cir_pacientes.count(i) for i in range(1,len(vale)+1)]
    for j in range(len(vale)):
        lista+=[[vale[j],contador[j]]]

    hola=[["Cirugias","Cantidad"]]
    lista=hola+lista
    
    modified_data=json.dumps(lista)

    return render(request,'graph_cirugia.html',{    
        'values':modified_data,
    })

def medicamento(request):
    todos_medicamentos=medicamentos.objects.values_list('nombre',flat=True)
    usados_medicamentos=hoja_indicaciones.objects.values_list('nombre_medicamento',flat=True)

    return render(request,'KPI.html',{
        'values':usados_medicamentos,
    })
