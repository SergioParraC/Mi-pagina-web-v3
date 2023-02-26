from django.contrib import admin
from django.urls import path, re_path
from mipagweb_v3.views import inicio
from gestion_HV import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name="index"),
    path('companies/<int:id_comp>',views.company_page, name='companies'),
    path('test/<int:id_comp>',views.test),
    path('acerca-de/', views.about, name='about'),
    path('experiencia/<int:id_exp>',views.experiencies_page, name='experiences'),
    path('proyectos/<int:id_proj>', views.projects_page, name='projects'),
    path('educacion/<int:id_ed>', views.education_page, name='education'),
    path('detalles/', views.details_page, name='details'),
    ]

urlpatterns += [
    re_path(r'^educacion/(?P<path>.*)', serve, {
        'document_root':settings.MEDIA_ROOT,
    })
]