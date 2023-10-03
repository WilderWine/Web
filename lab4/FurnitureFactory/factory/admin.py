from django.contrib import admin

from .models import Furniture, FurnitureCategory, FurnitureCollection, Client
# Register your models here.




@admin.register(Furniture)
class ProductAdmin(admin.ModelAdmin):
    """
    register estate
    """
    list_display = ['name', 'code', 'image', 'description', 'category', 'collection',
                    'attributes']
    list_filter = ['category',
                   'collection']


@admin.register(FurnitureCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(FurnitureCollection)
class CollectionAdmin(admin.ModelAdmin):

    list_display = ['collection']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    register client
    """
    list_display = ['first_name', 'last_name',
                    'email',
                    'birth_date',
                    'phone',
                    'city', 'address', 'image']
