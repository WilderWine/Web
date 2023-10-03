from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
     path('', views.product_list, name='product_list'),
     path('about/', views.about),
     path('contacts/', views.contacts),
     path('main/', views.guest),
     path('privacy_policy/', views.privacy_policy),
     path('<int:id>', views.product_detail, name='product_detail'),
     path("create/", views.product_create),
     path("edit/<int:id>/", views.product_edit),
     path("delete/<int:id>/", views.product_delete),
     path('<str:product_type_name>/', views.product_list, name='product_list_by_category')]