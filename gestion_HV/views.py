from django.shortcuts import render
from .models import companies, languages_programing, experiencies, projects, profesional_education as education
from django.http import HttpResponse
import inflect
from django.db.models import Case, When, Value, IntegerField
import mimetypes

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

    def query_common(self, query):
        return companies.objects.values_list(query, flat=True).order_by('id')

class experience_details(object):

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
  
    def contact(self):
        name = experiencies.objects.values_list('contact', flat=True).order_by('-start_date')
        boss_post = experiencies.objects.values_list('position_boss', flat=True).order_by('-start_date')
        data=[]
        for i in range(len(name)):
            if boss_post:
                data.append(name[i])
            else:
                data.append(boss_post[i] + " " + name[i])
        return data
    
    def query_common(self, query):
        return experiencies.objects.values_list(query, flat=True).order_by('-start_date')

class projects_details(object):
    
    def query_common(self, query):
        return projects.objects.values_list(query, flat=True).order_by('-start_date')
    
    def date(self):
        select_data_month = {"m": """strftime('%%m', start_date)"""}
        data_start_month = projects.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-start_date')
        select_data_year = {"y": """strftime('%%Y', start_date)"""}
        data_start_year = projects.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-start_date')
        select_data_month = {"m": """strftime('%%m', ending_date)"""}
        data_end_month = projects.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-start_date')
        select_data_year = {"y": """strftime('%%Y', ending_date)"""}
        data_end_year = projects.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-start_date')
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
        data=projects.objects.values_list('company', flat=True).order_by('-start_date')
        data2=[]
        for i in data:
            data2.append(companies.objects.get(id=i))
        return data2
    
    def position(self):
        data=projects.objects.values_list('position', flat=True).order_by('-start_date')
        data2=[]
        for i in data:
            data2.append(experiencies.objects.values_list('position', flat=True).get(id=i))
        return data2

est=Case(
                When(type_estudy='Curso', then=Value(10)),
                When(type_estudy='Diplomado', then=Value(9)),
                When(type_estudy='Bachillerato', then=Value(1)),
                When(type_estudy='Tecnico', then=Value(2)),
                When(type_estudy='Tecnologo', then=Value(3)),
                When(type_estudy='Profesional', then=Value(4)),
                When(type_estudy='Especializaci??n', then=Value(5)),
                When(type_estudy='Maestria', then=Value(6)),
                When(type_estudy='Doctorado', then=Value(7)),
                When(type_estudy='Posdoctorado', then=Value(8)),
                output_field=IntegerField())

class education_details(object):
    
    def query_common(self, query):
        
        q=education.objects.values_list(query, flat=True).annotate(custom_order=est).order_by('start_date', 'custom_order')
        return q

    def date(self):
        select_data_month = {"m": """strftime('%%m', start_date)"""}
        data_start_month = education.objects.extra(select=select_data_month).values_list('m', flat=True).annotate(custom_order=est).order_by('-start_date')
        select_data_year = {"y": """strftime('%%Y', start_date)"""}
        data_start_year = education.objects.extra(select=select_data_year).values_list('y', flat=True).annotate(custom_order=est).order_by('-start_date')
        select_data_month = {"m": """strftime('%%m', ending_date)"""}
        data_end_month = education.objects.extra(select=select_data_month).values_list('m', flat=True).annotate(custom_order=est).order_by('-start_date')
        select_data_year = {"y": """strftime('%%Y', ending_date)"""}
        data_end_year = education.objects.extra(select=select_data_year).values_list('y', flat=True).annotate(custom_order=est).order_by('-start_date')
        data=[]
        for i in range(len(data_start_month)):
            j=data_start_month[i]
            k=data_end_month[i]
            if data_end_year[i]:
                data.append(mesesDic[k] + " " + str(data_end_year[i]))
            else:
                data.append(mesesDic[j] + " " + str(data_start_year[i]))
        return (data)

def projects_page(request, id_proj):
    if id_proj==0:
        id_proj=1
    proj=projects_details()
    data_titles=zip(proj.query_common('id'), proj.query_common('title'))
    data=zip(proj.query_common('id') , proj.date(), proj.position(), proj.query_common('progress'), proj.query_common('address'), proj.query_common('city'),  proj.query_common('description'),proj.query_common('web_page'), proj.company(), proj.query_common('company'))
    return render(request, "projects.html", {'data_titles':data_titles, 'data':data, 'id_activate':id_proj})

def about(request):
    return render(request, "about.html")

def experiencies_page(request, id_exp):
    if id_exp==0:
        id_exp=1
    exp_det=experience_details()
    data_nav=zip(exp_det.query_common('id'),exp_det.query_common('position'))
    data=zip(exp_det.query_common('id'), exp_det.query_common('position'), exp_det.date(), exp_det.company(), exp_det.query_common('company'), exp_det.query_common('description'), exp_det.query_common('city'), exp_det.contact(), exp_det.query_common('phone'), exp_det.query_common('email'), exp_det.query_common('certificate'))
    return render(request, "experiencie.html",{"data_nav":data_nav,"data":data,"id_activate":id_exp})

def company_page(request, id_comp):
    if id_comp==0:
        id_comp=1
    comp=companies_details()
    p = inflect.engine()
    cap_id=p.number_to_words(id_comp)
    capital=cap_id.capitalize()
    data=zip(comp.query_common('name'), comp.title(), comp.collapse_number(), comp.query_common('legal_rep'), comp.query_common('city'), comp.query_common('addres'), comp.query_common('phone'), comp.query_common('email'), comp.query_common('web_page'))
    return render(request, "companies.html",{"data":data,"cap_id":capital})

def education_page(request, id_ed):
    if id_ed==0:
        id_ed=1
    edc=education_details()
    data_nav=zip(edc.query_common('id'),edc.query_common('title'))
    data=zip(edc.query_common('id'), edc.query_common('type_estudy'), edc.query_common('institute'),  edc.query_common('city'), edc.date(), edc.query_common('web_page'), edc.query_common('description'), edc.query_common('certificate'), edc.query_common('diploma'))
    #return HttpResponse(data)
    return render(request, "education.html", {"data_nav":data_nav, "data":data ,"id_activate":id_ed})
    
def details_page(request):
    return render(request, "details.html")
