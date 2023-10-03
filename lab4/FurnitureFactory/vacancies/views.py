from django.shortcuts import render
from .models import Vacancy


# Create your views here.


def vacancies(request):

    vacs = Vacancy.objects.all()

    context = {'vacancies': vacs}

    return render(request, 'vacancies/vacancies.html', context)