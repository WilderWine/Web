from django.shortcuts import render
from .models import Faq

# Create your views here.


def faq(request):
    faqs = Faq.objects.all().order_by('-created')
    context = {'faqs': faqs}
    return render(request, 'faq/faq.html', context)

