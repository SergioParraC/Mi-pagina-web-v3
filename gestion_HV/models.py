from django.db import models
from gestion_HV import choises

class profesional_education(models.Model):

    title=models.CharField(max_length=100, verbose_name="Titulo")
    institute=models.CharField(max_length=100, verbose_name="Instituto educativo")
    start_date=models.DateField(verbose_name="Fecha de inicio")
    ending_date=models.DateField(null=True, blank=True, verbose_name="Fecha final")
    web_page=models.CharField(max_length=75, verbose_name="Pagina web")
    diploma=models.FileField(upload_to='fields/', max_length=100, null=True, blank=True, verbose_name="Adjuntar diploma")
    certificate=models.BooleanField(verbose_name="Está certificado el titulo?")
    description=models.TextField(null=True, blank=True, verbose_name="Descripción del curso")
    type_estudy=models.CharField(max_length=75, verbose_name="Tipo de estudio", choices=choises.TTITLES_STUDIES_CHOICES)
    city=models.CharField(max_length=50, verbose_name="Ciudad - municipio")


    class Meta:
        verbose_name="Estudio profesional"
        verbose_name_plural="Estudios profesionales"
        ordering=['start_date']

    def __str__(self):
        return "%s en %s" % (self.title, self.institute)

class companies(models.Model):
    
    name=models.CharField(max_length=75, verbose_name="Nombre")
    legal_rep=models.CharField(max_length=75, verbose_name="Representante Legal")
    city=models.CharField(max_length=25, verbose_name="Ciudad")
    sector=models.CharField(max_length=25, verbose_name="Sector")
    area=models.CharField(max_length=50, verbose_name="Área de trabajo")
    addres=models.CharField(max_length=40, verbose_name="Dirección")
    web_page=models.CharField(max_length=75, null=True, blank=True, verbose_name="Pagina Web")
    email=models.EmailField(max_length=254, verbose_name="Correo electronico")
    phone=models.CharField(max_length=10, verbose_name='Numero telefonico')

    class Meta:
        verbose_name="Empresa"
        verbose_name_plural="Empresas"
        ordering=['name']

    def __str__(self):
        return self.name

class experiencies(models.Model):

    position=models.CharField(max_length=50, verbose_name="Cargo")
    start_date=models.DateField(verbose_name="Fecha de inicio")
    ending_date=models.DateField(null=True, blank=True, verbose_name="Fecha final")
    company=models.OneToOneField(companies, on_delete=models.CASCADE, verbose_name="Compañia") #Relacion uno a uno entre la experiencia con la compañia donde se hizo la experiencia 
    description=models.TextField(verbose_name="Descripción del cargo")
    contact=models.CharField(max_length=150,verbose_name="Nombre de jefe directo")
    phone=models.CharField(max_length=10, verbose_name="Telefono de contacto")
    email=models.EmailField(max_length=254, verbose_name="Correo electronico")
    city=models.CharField(max_length=25, verbose_name="Ciudad")
    estudies=models.ManyToManyField(profesional_education, verbose_name="Estudios utilizados") #Relación muchos a muchos entre las experiencias y los estudios realizados
    position_boss=models.CharField(max_length=25, null=True, blank=True)
    boss=models.CharField(max_length=75, null=True, blank=True)

    class Meta:
        verbose_name="Experiencia"
        verbose_name_plural="Experiencias"
        ordering=['start_date']

    def __str__(self):
        return '%s en %s' % (self.position, self.company)

class languages_programing(models.Model):
    
    name=models.CharField(max_length=50, verbose_name="Nombre")
    date=models.DateField(verbose_name="Fecha")
    level=models.CharField(max_length=50, verbose_name="Nivel de progreso", choices=choises.LEVEL_CHOICES)
    class_icon=models.CharField(max_length=100, verbose_name="Clase del lenguaje o enlace")
    web_page=models.CharField(max_length=75, verbose_name="Pagina Web oficial")
    have_icon=models.BooleanField(verbose_name="Tiene icono?")

    class Meta:
        verbose_name="Lenguaje de programación"
        verbose_name_plural="Lenguajes de programación"
        ordering=['date']

    def __str__(self):
        return self.name

class projects(models.Model):

    title=models.CharField(max_length=150, verbose_name="Titulo del proyecto")
    start_date=models.DateField(verbose_name="Fecha inicio del proyecto")
    ending_date=models.DateField(null=True, blank=True, verbose_name="Fecha fin del proyecto")
    position=models.ForeignKey(experiencies, on_delete=models.CASCADE, verbose_name="Cargo") #Relación uno a mucjos de los proyectos con una sola experiencia
    city=models.CharField(max_length=50, verbose_name="Ciudad")
    web_page=models.CharField(max_length=250, null=True, blank=True, verbose_name="Pagina de internet")
    description=models.TextField(verbose_name="Descripción")
    address=models.CharField(max_length=100, verbose_name="Dirección o ubicación", null=True, blank=True)
    progress=models.CharField(max_length=50, verbose_name="Estado del proyecto")
    company=models.ForeignKey(companies, on_delete=models.CASCADE, verbose_name="Empresa") #Relación uno a muchos de los proyectos con una sola empresa
    tecnologias=models.ManyToManyField(languages_programing)

    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        ordering=['start_date']

    def __str__(self):
        return self.title