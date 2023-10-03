from django.shortcuts import render
import requests

# Create your views here.


def useapis(request):

    catfact = requests.get('https://catfact.ninja/fact').json()['fact']

    gender = requests.get(f'https://api.genderize.io/?name={request.user.first_name}').json()['gender']

    dogimage = requests.get(f'https://dog.ceo/api/breeds/image/random').json()['message']

    return render(request, 'apistuff/api_results.html', {'catfact':catfact, 'gender':gender, 'dogimage':dogimage})