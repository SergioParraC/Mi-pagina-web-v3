from django.shortcuts import render
from .models import companies, languages_programing, experiencies
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

def company_page(request, id_comp):
    comp=companies_details()
    p = inflect.engine()
    cap_id=p.number_to_words(id_comp)
    capital=cap_id.capitalize()
    data=zip(comp.name(), comp.title(), comp.collapse_number(), comp.legal_rep(), comp.city(), comp.addres(), comp.phone(), comp.email(), comp.web_page())
    
    return render(request, "companies.html",{"data":data,"cap_id":capital})

class experience_details(object):
    def position(self):
        return experiencies.objects.values_list('position', flat=True).order_by('-start_date')
    def id(self):
        return experiencies.objects.values_list('id', flat=True).order_by('-start_date')
    def date(self):
        select_data_month = {"m": """strftime('%%m', start_date)"""}
        data_start_month = experiencies.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-start_date')
        select_data_year = {"y": """strftime('%%Y', start_date)"""}
        data_start_year = experiencies.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-start_date')
        select_data_month = {"m": """strftime('%%m', ending_date)"""}
        data_end_month = experiencies.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-start_date')
        select_data_year = {"y": """strftime('%%Y', ending_date)"""}
        data_end_year = experiencies.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-start_date')
        data=[]
        for i in range(len(data_start_month)):
            j=data_start_month[i]
            k=data_end_month[i]
            if data_end_year[i]:
                data.append(mesesDic[j] + " " + str(data_start_year[i]) + " - " + mesesDic[k] + " " + str(data_end_year[i]))
            else:
                data.append(mesesDic[j] + " " + str(data_start_year[i]))
        return (data)
    def company(self):
        data=experiencies.objects.values_list('company', flat=True).order_by('-start_date')
        data3=[]
        for i in data:
            data3.append(companies.objects.get(id=i))
        return data3
    def company_id(self):
        return experiencies.objects.values_list('company', flat=True).order_by('-start_date')

    def description(self):
        return experiencies.objects.values_list('description', flat=True).order_by('-start_date')
    
    def contact(self):
        name = experiencies.objects.values_list('contact', flat=True).order_by('-start_date')
        boss_post = experiencies.objects.values_list('position_boss', flat=True).order_by('-start_date')
        data=[]
        for i in range(len(name)):
            data.append(boss_post[i] + " " + name[i])
        return data

    def phone(self):
        return experiencies.objects.values_list('phone', flat=True).order_by('-start_date')

    def email(self):
        return experiencies.objects.values_list('email', flat=True).order_by('-start_date')

    def city(self):
        return experiencies.objects.values_list('city', flat=True).order_by('-start_date')



def about(request):
    return render(request, "about.html")

def experiencies_page(request, id_exp):
    exp_det=experience_details()
    data_nav=zip(exp_det.id(),exp_det.position())
    data=zip(exp_det.id(), exp_det.position(), exp_det.date(), exp_det.company(), exp_det.company_id(), exp_det.description(), exp_det.city(), exp_det.contact(), exp_det.phone(), exp_det.email())
    return render(request, "experiencie.html",{"data_nav":data_nav,"data":data,"id_activate":id_exp})

def test(request, id_comp):
    comp=companies_details()
    p = inflect.engine()
    cap_id=p.number_to_words(id_comp)
    capital=cap_id.capitalize()
    return HttpResponse(capital)