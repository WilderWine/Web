from django.urls import path
from . import views

app_name = 'apistuff'

urlpatterns = [
    path('', views.useapis, name='api_results'),
]