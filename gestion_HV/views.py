from django.shortcuts import render
from .models import profesional_education
from django.http import HttpResponse
from django.db.models.functions import Extract
from datetime import datetime


def test(request):
    data=profesional_education.objects.annotate(start_year=Extract('start_date','year'))
    
    return HttpResponse(data)

    