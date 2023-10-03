from django.contrib import admin
from .models import Promo

# Register your models here.


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    """
    register comments nstanse
    """
    list_display = ['promocode', 'slogan', 'is_active', 'description', 'created']
    list_filter = ['is_active']

