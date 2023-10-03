from django.contrib import admin

# Register your models here.
from .models import Vacancy

# Register your models here.


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """
    register comments nstanse
    """
    list_display = ['position', 'description', 'requirements', 'created']

