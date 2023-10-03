from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.comments, name='all_comments'),
    path('add_comment/', views.add_comment, name='add_comment')
]
