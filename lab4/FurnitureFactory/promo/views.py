from django.shortcuts import render
from .models import Promo

# Create your views here.


def promo(request):
    promos = Promo.objects.all()

    return render(request, 'promo/promo.html', {'promos': promos})
