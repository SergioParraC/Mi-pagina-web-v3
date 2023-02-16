from django.http import HttpResponse
from django.template import Template, Context

class courses_info(object):

    def course_name(self):
        return ["Curso profesional de Python","Aprende Microsoft Project 2019"]
    def course_date(self):
        return ["Julio 2022","Julio 2022"]
    def course_institute(self):
        return ["Códigofacilito","Udemy"]

def inicio(request): #Primera vista
    courses_list=courses_info()
    course_name=courses_list.course_name()
    course_date=courses_list.course_date()
    course_institute=courses_list.course_institute()
    cour=zip(course_name,course_date,course_institute)
    doc_externo = open("/mnt/c/Users/djson/Desktop/Programacion/Proyectos/mipagweb_v3/mipagweb_v3/templates/index.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"first_name":"Sergio Steven","courses":cour})
    documento=plt.render(ctx)
    return HttpResponse(documento)