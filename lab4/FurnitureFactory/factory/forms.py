from django import forms

from .models import Furniture


class ProductForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['name', 'price', 'code', 'image', 'description', 'category', 'collection', 'attributes']
