from django.shortcuts import render
from .models import experiencies, companies, profesional_education
from django.http import HttpResponse
from datetime import datetime
mesesDic = {
    "01":'ENERO',
    "02":'FEBRERO',
    "03":'MARZO',
    "04":'ABRIL',
    "05":'MAYO',
    "06":'JUNIO',
    "07":'JULIO',
    "08":'AGOSTO',
    "09":'SEPTIEMBRE',
    "10":'OCTUBRE',
    "11":'NOVIEMBRE',
    "12":'DICIEMBRE'
}
data2=[]
data3=[]
def test(request):
    return ()

