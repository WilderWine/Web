from django.contrib import admin
from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    register comments nstanse
    """
    list_display = ['client', 'created', 'rating', 'content']
