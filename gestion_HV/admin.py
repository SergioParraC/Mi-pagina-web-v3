from django.contrib import admin
from gestion_HV import models

class views_admin(admin.ModelAdmin):
    list_display=("__str__", "ending_date")

admin.site.register(models.profesional_education, views_admin)

admin.site.register(models.companies)

admin.site.register(models.experiencies, views_admin)

admin.site.register(models.languages_programing)

admin.site.register(models.projects, views_admin)