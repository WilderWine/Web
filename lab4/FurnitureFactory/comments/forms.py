from django import forms

from .models import Comment


RATING_CHOICES= [
    (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ]


class RatingForm(forms.Form):

    rating = forms.IntegerField(label='Rate our service', widget=forms.RadioSelect(choices=RATING_CHOICES))
    content = forms.Textarea()
