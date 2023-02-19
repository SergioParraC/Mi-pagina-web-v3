from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from gestion_HV.models import profesional_education, companies, experiencies, languages_programing, projects

class prof_education(object):

    def univercity(self):
        data=profesional_education.objects.values_list('institute', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        return data
    def date(self):
        data=profesional_education.objects.values_list('start_date', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        return data
    def title(self):
        data=profesional_education.objects.values_list('title', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        return data
    def city(self):
        data=profesional_education.objects.values_list('city', flat=True).order_by('-start_date').exclude(type_estudy='CUR')
        return data

class experience_info(object):

    def position(self):
        return experiencies.objects.values_list('position', flat=True).order_by('-start_date')
    def date(self):
        return experiencies.objects.values_list('start_date', flat=True).order_by('-start_date')
    def company(self):
        return experiencies.objects.values_list('company', flat=True).order_by('-start_date')
    def description(self):
        return experiencies.objects.values_list('description', flat=True).order_by('-start_date')
    def position_boss(self):
        return experiencies.objects.values_list('position_boss', flat=True).order_by('-start_date')
    def boss(self):
        return experiencies.objects.values_list('contact', flat=True).order_by('-start_date')
    def cell(self):
        return experiencies.objects.values_list('contact', flat=True).order_by('-start_date')
    def email(self):
        return experiencies.objects.values_list('email', flat=True).order_by('-start_date')

class courses_info(object):

    def name(self):
        return profesional_education.objects.filter(type_estudy='CUR').values_list('title', flat=True)
    def date(self):
        return profesional_education.objects.filter(type_estudy='CUR').values_list('start_date', flat=True)
    def institute(self):
        return profesional_education.objects.filter(type_estudy='CUR').values_list('institute', flat=True)

class languages_soft(object):

    def name(self):
        return languages_programing.objects.values_list('name', flat=True).order_by('-date')
    def icon_class(self):
        return languages_programing.objects.values_list('class_icon', flat=True).order_by('-date')
    def date(self):
        return languages_programing.objects.values_list('date', flat=True).order_by('-date')

class projects_info(object):
    def title(self):
        return projects.objects.values_list('title', flat=True).order_by('-start_date')
    def date(self):
        return projects.objects.values_list('start_date', flat=True).order_by('-start_date')
    def position(self):
        return projects.objects.values_list('position', flat=True).order_by('-start_date')
    def address(self):
        return projects.objects.values_list('start_date', flat=True).order_by('-start_date')
    def description(self):
        return projects.objects.values_list('description', flat=True).order_by('-start_date')
    def status(self):
        return projects.objects.values_list('progress', flat=True).order_by('-start_date')

def inicio(request): #Primera vista
    
    ex_list=experience_info()
    experience=zip(ex_list.position(), ex_list.date(), ex_list.company(), ex_list.description(), ex_list.position_boss(), ex_list.boss(), ex_list.cell(),ex_list.email())

    prof_study_list=prof_education()
    prof_ed=zip(prof_study_list.univercity(), prof_study_list.date(), prof_study_list.title(), prof_study_list.city())

    courses_list=courses_info()
    courses=zip(courses_list.name(), courses_list.date(), courses_list.institute())

    lang_soft_list=languages_soft()
    languages_software=zip(lang_soft_list.name(), lang_soft_list.icon_class(), lang_soft_list.date())

    proyects_list=projects_info()
    proyects=zip(proyects_list.title(),proyects_list.date(),proyects_list.position(),proyects_list.address(),proyects_list.description(),proyects_list.status())

    

    return render(request, "index.html", {"experience":experience, "courses":courses, "prof_study":prof_ed, "languages_software":languages_software, "proyects":proyects})
