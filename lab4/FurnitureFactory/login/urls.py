from . import views
from django.urls import path

app_name = 'login'

urlpatterns = [

    path('logout/',
         views.LogOutView.as_view(),
         name='logout'),
path('login/',
         views.LoginFormView.as_view(),
         name='login'),
    path('signup/',
         views.SignUpFormView.as_view(),
         name='signup')
]
