from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

class prof_education(object):

    def univercity(self):
        return ["Universidad Católica de Colombia","Colegio Católico de la Sabana"]
    def date(self):
        return ["Enero 2015 - Abril 2020","Diciembre 2014"]
    def title(self):
        return ["Ingeniero Civil","Básico bachillerato"]
    def city(self):
        return ["BOGOTÁ - COLOMBIA","BOGOTÁ - COLOMBIA"]

class experience_info(object):

    def position(self):
        return ["Cartógrafo","Dibujante"]
    def date(self):
        return ["Febrero 2019 - Junio 2019","Agosto 2017 - Octubre 2017"]
    def company(self):
        return ["Proindesco LTDA","Trabaho independiente"]
    def description(self):
        return ["Análisis de datos geográficos para localizar cuencas, cálculo de sus parametros básicos para el diseño de sistemas de recoleccion de agua potable.","Dibujo de planos hidráulicos, sanitarios y eléctricos para presentación al dueño de la obra."]
    def position_boss(self):
        return ["Ing","Ing"]
    def boss(self):
        return ["Guilermo Hernandez Torrez","Fabián Ancizar Barreto"]
    def cell(self):
        return [3157274724,3013114723]
    def email(self):
        return ["ghernandez@ucatolica.edu.co","fabarreto22@ucatolica.edu.co"]

class courses_info(object):

    def name(self):
        return ["Curso profesional de Python","Aprende Microsoft Project 2019"]
    def date(self):
        return ["Julio 2022","Julio 2022"]
    def institute(self):
        return ["Códigofacilito","Udemy"]

class languages_soft(object):

    def name(self):
        return ["Bootstrap V 4.0","Git","MySQL","php"]
    def icon_class(self):
        return ["devicon-bootstrap-plain","devicon-git-plain","devicon-mysql-plain-wordmark","devicon-php-plain"]
    def date(self):
        return ["Diciembre 2020","Noviembre 2020","Noviembre 2020","Noviembre 2020"]

class projects(object):
    def title(self):
        return ["DISEÑO DE PAGINA WEB PERSONAL Version 1.0", "TRABAJO DE GRADO"]
    def date(self):
        return ["Septiembre 2020", "Noviembre 2019"]
    def position(self):
        return ["Sergio Parra - Perfil", "Análisis de oferta hídrica superficial a escala diaria aplicada en cuencas colombianas"]
    def address(self):
        return ["https://sergioparrac.github.io/Portfolio-V-1.0/","https://sergioparrac.github.io/Portfolio-V-1.0/"]
    def description(self):
        return ["En este aplíco lo que aprendí de estructura con HTML, uso de etiquetas en CSS3, programación en JavaScrip para interaciones dentro de la página y Jquery para llamado de objetos y tratamiento de sus caracteristicas","Trabajo para optar el titulo de Ingeniero civil. En el uso la modelación y el tratamiento de datos para el calculo de escorrentia superficial sobre las cuencas de rio Coello en Ibagué - Tolima y rio Ceibas en Neiva - Huila"]
    def status(self):
        return ["Culminado", "Culminado"]

def inicio(request): #Primera vista
    ex_list=experience_info()
    experience=zip(ex_list.position(), ex_list.date(), ex_list.company(), ex_list.description(), ex_list.position_boss(), ex_list.boss(), ex_list.cell(),ex_list.email())

    prof_study=prof_education()
    profesional_education=zip(prof_study.univercity(), prof_study.date(), prof_study.title(), prof_study.city())

    courses_list=courses_info()
    courses=zip(courses_list.name(), courses_list.date(), courses_list.institute())

    lang_soft_list=languages_soft()
    languages_software=zip(lang_soft_list.name(), lang_soft_list.icon_class(), lang_soft_list.date())

    proyects_list=projects()
    proyects=zip(proyects_list.title(),proyects_list.date(),proyects_list.position(),proyects_list.address(),proyects_list.description(),proyects_list.status())

    return render(request, "index.html", {"experience":experience, "courses":courses, "prof_study":profesional_education, "languages_software":languages_software, "proyects":proyects})