# Generated by Django 3.2.9 on 2023-02-18 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Nombre')),
                ('legal_rep', models.CharField(max_length=75, verbose_name='Representante Legal')),
                ('city', models.CharField(max_length=25, verbose_name='Ciudad')),
                ('sector', models.CharField(max_length=25, verbose_name='Sector')),
                ('area', models.CharField(max_length=50, verbose_name='Área de trabajo')),
                ('addres', models.CharField(max_length=40, verbose_name='Dirección')),
                ('web_page', models.CharField(blank=True, max_length=75, null=True, verbose_name='Pagina Web')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('phone', models.CharField(max_length=10, verbose_name='Numero telefonico')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='experiencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50, verbose_name='Cargo')),
                ('start_date', models.DateField(verbose_name='Fecha de inicio')),
                ('ending_date', models.DateField(blank=True, null=True, verbose_name='Fecha final')),
                ('description', models.TextField(verbose_name='Descripción del cargo')),
                ('contact', models.CharField(max_length=150, verbose_name='Nombre de jefe directo')),
                ('phone', models.CharField(max_length=10, verbose_name='Telefono de contacto')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('city', models.CharField(max_length=25, verbose_name='Ciudad')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_HV.companies', verbose_name='Compañia')),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='languages_programing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('level', models.CharField(max_length=50, verbose_name='Nivel de progreso')),
                ('class_icon', models.CharField(max_length=100, verbose_name='Clase del lenguaje o enlace')),
                ('web_page', models.CharField(max_length=75, verbose_name='Pagina Web oficial')),
                ('have_icon', models.BooleanField(verbose_name='Tiene icono?')),
            ],
            options={
                'verbose_name': 'Lenguaje de programación',
                'verbose_name_plural': 'Lenguajes de programación',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='profesional_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('institute', models.CharField(max_length=100, verbose_name='Instituto educativo')),
                ('start_date', models.DateField(verbose_name='Fecha de inicio')),
                ('ending_date', models.DateField(blank=True, null=True, verbose_name='Fecha final')),
                ('web_page', models.CharField(max_length=75, verbose_name='Pagina web')),
                ('diploma', models.FileField(blank=True, null=True, upload_to='fields/', verbose_name='Adjuntar diploma')),
                ('certificate', models.BooleanField(verbose_name='Está certificado el titulo?')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción del curso')),
                ('type_estudy', models.CharField(choices=[('CUR', 'Curso'), ('DIP', 'Diplomado'), ('BHL', 'Bachillerato'), ('TEC', 'Tecnico'), ('TEG', 'Tecnologo'), ('PRO', 'Profesional'), ('ESP', 'Especialización'), ('MAE', 'Maestria'), ('DOC', 'Doctorado'), ('POS', 'Posdoctorado')], max_length=75, verbose_name='Tipo de estudio')),
            ],
            options={
                'verbose_name': 'Estudio profesional',
                'verbose_name_plural': 'Estudios profesionales',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo del proyecto')),
                ('start_date', models.DateField(verbose_name='Fecha inicio del proyecto')),
                ('ending_date', models.DateField(blank=True, null=True, verbose_name='Fecha fin del proyecto')),
                ('web_page', models.CharField(blank=True, max_length=250, null=True, verbose_name='Pagina de internet')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('progress', models.CharField(max_length=50, verbose_name='Estado del proyecto')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_HV.companies', verbose_name='Empresa')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_HV.experiencies', verbose_name='Cargo')),
                ('tecnologias', models.ManyToManyField(to='gestion_HV.languages_programing')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['start_date'],
            },
        ),
        migrations.AddField(
            model_name='experiencies',
            name='estudies',
            field=models.ManyToManyField(to='gestion_HV.profesional_education', verbose_name='Estudios utilizados'),
        ),
    ]
