from django.shortcuts import render
from HojaIndicacion.models import paciente, hoja_indicaciones

# Create your views here.

def kpis(request):
    embarazo=paciente.objects.all()

    return render(request, 'KPI.html',{
        'embarazadas': embarazo
    })