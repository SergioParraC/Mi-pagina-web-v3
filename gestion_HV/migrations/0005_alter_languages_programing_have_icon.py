# Generated by Django 3.2.9 on 2023-02-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_HV', '0004_auto_20230227_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languages_programing',
            name='have_icon',
            field=models.CharField(choices=[('dev_icon', 'Icono en devicon.dev'), ('iconify_icon', 'Icono en iconify.design'), ('image', 'Imagen')], max_length=75, verbose_name='Que tipo de icono?'),
        ),
    ]
