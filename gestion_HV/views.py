from django.shortcuts import render
from .models import companies, languages_programing
from django.http import HttpResponse
import inflect

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

class companies_details(object):

    def name(self):
        return companies.objects.values_list('name', flat=True).order_by('id')
    
    def title(self):
        sector=companies.objects.values_list('sector', flat=True).order_by('id')
        area=companies.objects.values_list('area', flat=True).order_by('id')
        data=[]
        for i in range(0,len(sector)):
            data.append(sector[i] + " - " + area [i])
        return data

    def collapse_number(self):
        id_num=companies.objects.values_list('id', flat=True).order_by('id')
        p = inflect.engine()
        id_text=[]
        for i in id_num:
            capital=p.number_to_words(i)
            id_text.append(capital.capitalize())
        return id_text

    def legal_rep(self):
        return companies.objects.values_list('legal_rep', flat=True).order_by('id')

    def city(self):
        return companies.objects.values_list('city', flat=True).order_by('id')

    def addres(self):
        return companies.objects.values_list('addres', flat=True).order_by('id')

    def phone(self):
        return companies.objects.values_list('phone', flat=True).order_by('id')

    def email(self):
        return companies.objects.values_list('email', flat=True).order_by('id')

    def web_page(self):
        return companies.objects.values_list('web_page', flat=True).order_by('id')


def company(request):
    comp=companies_details()
    data=zip(comp.name(), comp.title(), comp.collapse_number(), comp.legal_rep(), comp.city(), comp.addres(), comp.phone(), comp.email(), comp.web_page())
    
    return render(request, "companies.html",{"data":data})

def test(request):
    id_num=companies.objects.values_list('id', flat=True).order_by('id')
    p = inflect.engine()
    id_text=[]
    for i in id_num:
        capital=p.number_to_words(i)
        id_text.append(capital.capitalize())
    return HttpResponse(id_text)