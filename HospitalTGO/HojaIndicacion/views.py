from django.shortcuts import render
from HojaIndicacion.models import paciente, hoja_indicaciones

# Create your views here.

def kpis(request):
    embarazo=paciente.objects.filter(embarazada=True)
    no_embarazo=paciente.objects.filter(embarazada=False)
    cirugias=hoja_indicaciones.objects.all()

    return render(request, 'KPI.html',{
        'embarazo': embarazo,
        'no_embarazo':no_embarazo,
        'cirugias': cirugias
    })