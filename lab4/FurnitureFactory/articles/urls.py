from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.news, name='all_news'),

    path('<int:article_id>/', views.current_article, name='current_news')
]
