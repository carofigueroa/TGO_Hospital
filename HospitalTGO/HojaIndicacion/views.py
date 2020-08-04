from django.shortcuts import render

# Create your views here.
from HojaIndicacion.models import paciente, hoja_indicaciones, cirugias
import json
# Create your views here.

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

    h_var="Cirugias"
    v_var="Cantidad"
    hola=[[h_var,v_var]]
    lista=hola+lista
    
    h_var_JSON=json.dumps(h_var)
    v_var_JSON=json.dumps(v_var)
    modified_data=json.dumps(lista)


    return render(request,'graph_cirugia.html',{    
        'values':modified_data,
        'h_title':h_var_JSON,
        'v_title':v_var_JSON


    })

def main(request):
    return render(request,'main.html')


def medicamentos(request):
    return render(request,'graph_med.html')
