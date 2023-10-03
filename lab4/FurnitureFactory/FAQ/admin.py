from django.contrib import admin
from .models import Faq

# Register your models here.


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    """
    register comments nstanse
    """
    list_display = ['question', 'answer', 'created']

