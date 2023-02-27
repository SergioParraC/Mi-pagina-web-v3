from django.template import Template, Context, loader
from django.shortcuts import render
from gestion_HV.models import profesional_education, companies, experiencies, languages_programing, projects
from datetime import datetime
from django.db.models import Q

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
excl=['Curso', 'Diplomado']
class prof_education(object):

    def query_common(self, query):
        return profesional_education.objects.values_list(query, flat=True).order_by('-start_date').exclude(type_estudy__in=excl)
    
    def date(self):
        select_data_month1 = {"m": """strftime('%%m', ending_date)"""}
        data_month = profesional_education.objects.extra(select=select_data_month1).values_list('m', flat=True).order_by('-start_date').exclude(type_estudy__in=excl)
        select_data_year1 = {"y": """strftime('%%Y', ending_date)"""}
        data_year = profesional_education.objects.extra(select=select_data_year1).values_list('y', flat=True).order_by('-start_date').exclude(type_estudy__in=excl)
        data2=[]
        data2.clear()
        for i in range(len(data_month)):
            j=data_month[i]
            data2.append(mesesDic[j] + " " + str(data_year[i]))
        return data2

class experience_info(object):

    def query_common(self, query):
        return experiencies.objects.values_list(query, flat=True).order_by('-start_date')
    
    def date(self):
        select_data_month = {"m": """strftime('%%m', start_date)"""}
        data_start_month = experiencies.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-start_date')
        select_data_year = {"y": """strftime('%%Y', start_date)"""}
        data_start_year = experiencies.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-start_date')
        select_data_month = {"m": """strftime('%%m', ending_date)"""}
        data_end_month = experiencies.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-start_date')
        select_data_year = {"y": """strftime('%%Y', ending_date)"""}
        data_end_year = experiencies.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-start_date')
        data3=[]
        for i in range(len(data_start_month)):
            j=data_start_month[i]
            k=data_end_month[i]
            if data_end_year[i]:
                data3.append(mesesDic[j] + " " + str(data_start_year[i]) + " - " + mesesDic[k] + " " + str(data_end_year[i]))
            else:
                data3.append(mesesDic[j] + " " + str(data_start_year[i]))
        return (data3)
    
    def company(self):
        data=self.query_common('company')
        data2=[]
        for i in data:
            data2.append(companies.objects.get(id=i))
        return data2

class courses_info(object):

    def query_common(self, query):
        return profesional_education.objects.filter(Q(type_estudy='Curso')|Q(type_estudy='Diplomado')).values_list(query, flat=True)
    
    def date(self):
        select_data_month = {"m": """strftime('%%m', start_date)"""}
        data_month = profesional_education.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-start_date').filter(Q(type_estudy='Curso')|Q(type_estudy='Diplomado'))
        select_data_year = {"y": """strftime('%%Y', start_date)"""}
        data_year = profesional_education.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-start_date').filter(Q(type_estudy='Curso')|Q(type_estudy='Diplomado'))
        data4=[]
        for i in range(len(data_month)):
            j=data_month[i]
            data4.append(mesesDic[j] + " " + str(data_year[i]))
        return data4

class languages_soft(object):

    def query_common(self, query):
        return languages_programing.objects.values_list(query, flat=True).order_by('-date')

    def date(self):
        select_data_month = {"m": """strftime('%%m', date)"""}
        data_month = languages_programing.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-date')
        select_data_year = {"y": """strftime('%%Y', date)"""}
        data_year = languages_programing.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-date')
        data5=[]
        for i in range(len(data_month)):
            j=data_month[i]
            data5.append(mesesDic[j] + " " + str(data_year[i]))
        return data5

class projects_info(object):

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
        data3=[]
        for i in range(len(data_start_month)):
            j=data_start_month[i]
            k=data_end_month[i]
            data3.append(mesesDic[j] + " " + str(data_start_year[i]) + " - " + mesesDic[k] + " " + str(data_end_year[i]))
        return (data3)
    
    def position(self):
        data=self.query_common('position')
        data2=[]
        for i in data:
            data2.append(experiencies.objects.values_list('position', flat=True).get(id=i))
        return data2
    
    def contact_data(self):
        data=self.query_common('position')
        data3=[]
        for i in data:
            j= experiencies.objects.values_list('contact', flat=True).get(id=i)
            k= experiencies.objects.values_list('phone', flat=True).get(id=i)
            l = experiencies.objects.values_list('position_boss', flat=True).get(id=i)
            if l:
                data3.append(l + " " + j + " - (+57) " + k)
            else:
                data3.append(j + " - (+57) " + k)
        return data3

def inicio(request): #Primera vista
    
    ex_list=experience_info()
    experience=zip(ex_list.query_common('position'), ex_list.date(), ex_list.company(), ex_list.query_common('description'), ex_list.query_common('position_boss'), ex_list.query_common('contact'), ex_list.query_common('phone'),ex_list.query_common('email'),ex_list.query_common('company'),ex_list.query_common('id'))

    prof_study_list=prof_education()
    prof_ed=zip(prof_study_list.query_common('id'),prof_study_list.query_common('institute'), prof_study_list.date(), prof_study_list.query_common('title'), prof_study_list.query_common('city'))

    courses_list=courses_info()
    courses=zip(courses_list.query_common('id'),courses_list.query_common('title'), courses_list.date(), courses_list.query_common('institute'))

    lang_soft_list=languages_soft()
    languages_software=zip(lang_soft_list.query_common('name'), lang_soft_list.query_common('class_icon'), lang_soft_list.date())

    proyects_list=projects_info()
    proyects=zip(proyects_list.query_common('id'), proyects_list.query_common('title'),proyects_list.date(),proyects_list.position(),proyects_list.query_common('address'),proyects_list.query_common('description'),proyects_list.query_common('progress'),proyects_list.query_common('web_page'),proyects_list.contact_data())
 
    return render(request, "index.html", {"experience":experience, "courses":courses, "prof_study":prof_ed, "languages_software":languages_software, "proyects":proyects})
