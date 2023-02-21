from django.template import Template, Context, loader
from django.shortcuts import render
from gestion_HV.models import profesional_education, companies, experiencies, languages_programing, projects
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

class prof_education(object):

    def univercity(self):
        data=profesional_education.objects.values_list('institute', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        return data
    def date(self):
        select_data_month1 = {"m": """strftime('%%m', ending_date)"""}
        data_month = profesional_education.objects.extra(select=select_data_month1).values_list('m', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        select_data_year1 = {"y": """strftime('%%Y', ending_date)"""}
        data_year = profesional_education.objects.extra(select=select_data_year1).values_list('y', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        data2=[]
        data2.clear()
        for i in range(len(data_month)):
            j=data_month[i]
            data2.append(mesesDic[j] + " " + str(data_year[i]))
        return data2

    def title(self):
        data=profesional_education.objects.values_list('title', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        return data
    def city(self):
        data=profesional_education.objects.values_list('city', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        return data

class experience_info(object):

    def position(self):
        return experiencies.objects.values_list('position', flat=True).order_by('-start_date')
    def date2(self):
        select_data_month2 = {"m": """strftime('%%m', start_date)"""}
        data_start_month2 = experiencies.objects.extra(select=select_data_month2).values_list('m', flat=True).order_by('-start_date')
        select_data_year2 = {"y": """strftime('%%Y', start_date)"""}
        data_start_year2 = experiencies.objects.extra(select=select_data_year2).values_list('y', flat=True).order_by('-start_date')
        select_data_month2 = {"m": """strftime('%%m', ending_date)"""}
        data_end_month2 = experiencies.objects.extra(select=select_data_month2).values_list('m', flat=True).order_by('-start_date')
        select_data_year2 = {"y": """strftime('%%Y', ending_date)"""}
        data_end_year2 = experiencies.objects.extra(select=select_data_year2).values_list('y', flat=True).order_by('-start_date')
        data3=[]
        for i in range(len(data_start_month2)):
            j=data_start_month2[i]
            k=data_end_month2[i]
            data3.append(mesesDic[j] + " " + str(data_start_year2[i]) + " - " + mesesDic[k] + " " + str(data_end_year2[i]))
        return (data3)
    def company(self):
        data=experiencies.objects.values_list('company', flat=True).order_by('-start_date')
        data3=[]
        for i in data:
            data3.append(companies.objects.get(id=i))
        return data3
    def description(self):
        return experiencies.objects.values_list('description', flat=True).order_by('-start_date')
    def position_boss(self):
        return experiencies.objects.values_list('position_boss', flat=True).order_by('-start_date')
    def boss(self):
        return experiencies.objects.values_list('contact', flat=True).order_by('-start_date')
    def cell(self):
        return experiencies.objects.values_list('phone', flat=True).order_by('-start_date')
    def email(self):
        return experiencies.objects.values_list('email', flat=True).order_by('-start_date')

class courses_info(object):

    def name(self):
        return profesional_education.objects.filter(type_estudy='CUR').values_list('title', flat=True)
    def date(self):
        select_data_month = {"m": """strftime('%%m', start_date)"""}
        data_month = profesional_education.objects.extra(select=select_data_month).values_list('m', flat=True).order_by('-start_date').filter(type_estudy='CUR')
        select_data_year = {"y": """strftime('%%Y', start_date)"""}
        data_year = profesional_education.objects.extra(select=select_data_year).values_list('y', flat=True).order_by('-start_date').filter(type_estudy='CUR')
        data4=[]
        for i in range(len(data_month)):
            j=data_month[i]
            data4.append(mesesDic[j] + " " + str(data_year[i]))
        return data4
    def institute(self):
        return profesional_education.objects.filter(type_estudy='CUR').values_list('institute', flat=True)

class languages_soft(object):

    def name(self):
        return languages_programing.objects.values_list('name', flat=True).order_by('-date')
    def icon_class(self):
        return languages_programing.objects.values_list('class_icon', flat=True).order_by('-date')
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
    def title(self):
        return projects.objects.values_list('title', flat=True).order_by('-start_date')
    def date(self):
        select_data_month2 = {"m": """strftime('%%m', start_date)"""}
        data_start_month2 = projects.objects.extra(select=select_data_month2).values_list('m', flat=True).order_by('-start_date')
        select_data_year2 = {"y": """strftime('%%Y', start_date)"""}
        data_start_year2 = projects.objects.extra(select=select_data_year2).values_list('y', flat=True).order_by('-start_date')
        select_data_month2 = {"m": """strftime('%%m', ending_date)"""}
        data_end_month2 = projects.objects.extra(select=select_data_month2).values_list('m', flat=True).order_by('-start_date')
        select_data_year2 = {"y": """strftime('%%Y', ending_date)"""}
        data_end_year2 = projects.objects.extra(select=select_data_year2).values_list('y', flat=True).order_by('-start_date')
        data3=[]
        for i in range(len(data_start_month2)):
            j=data_start_month2[i]
            k=data_end_month2[i]
            data3.append(mesesDic[j] + " " + str(data_start_year2[i]) + " - " + mesesDic[k] + " " + str(data_end_year2[i]))
        return (data3)
    def position(self):
        data=projects.objects.values_list('position', flat=True).order_by('-start_date')
        data3=[]
        for i in data:
            data3.append(experiencies.objects.values_list('position', flat=True).get(id=i))
        return data3
    def address(self):
        return projects.objects.values_list('address', flat=True).order_by('-start_date')
    def description(self):
        return projects.objects.values_list('description', flat=True).order_by('-start_date')
    def status(self):
        return projects.objects.values_list('progress', flat=True).order_by('-start_date')
    def web_page(self):
        return projects.objects.values_list('web_page', flat=True).order_by('-start_date')
    def contact_data(self):
        data=projects.objects.values_list('position', flat=True).order_by('-start_date')
        data3=[]
        for i in data:
            j= experiencies.objects.values_list('contact', flat=True).get(id=i)
            k= experiencies.objects.values_list('phone', flat=True).get(id=i)
            data3.append(j + " - "+ k)
        return data3

def inicio(request): #Primera vista
    
    ex_list=experience_info()
    experience=zip(ex_list.position(), ex_list.date2(), ex_list.company(), ex_list.description(), ex_list.position_boss(), ex_list.boss(), ex_list.cell(),ex_list.email())

    prof_study_list=prof_education()
    prof_ed=zip(prof_study_list.univercity(), prof_study_list.date(), prof_study_list.title(), prof_study_list.city())

    courses_list=courses_info()
    courses=zip(courses_list.name(), courses_list.date(), courses_list.institute())

    lang_soft_list=languages_soft()
    languages_software=zip(lang_soft_list.name(), lang_soft_list.icon_class(), lang_soft_list.date())

    proyects_list=projects_info()
    proyects=zip(proyects_list.title(),proyects_list.date(),proyects_list.position(),proyects_list.address(),proyects_list.description(),proyects_list.status(),proyects_list.web_page(),proyects_list.contact_data())
 
    return render(request, "index.html", {"experience":experience, "courses":courses, "prof_study":prof_ed, "languages_software":languages_software, "proyects":proyects})
