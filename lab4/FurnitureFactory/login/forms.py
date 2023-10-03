from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ClientUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date


def validate_age(value):

    today = date.today()
    age = today.year - value.year - int((today.month, today.day) < (value.month, value.day))
    if int(age) < 18:
        raise ValidationError("You must be 18 or older to create an account")
    elif int(age) > 130:
        raise ValidationError("You seem to be extraordinarily old")


class UserCreateForm(UserCreationForm):

    first_name = forms.CharField(max_length=200,
                                 help_text='Name')
    last_name = forms.CharField(max_length=200,
                                 help_text='Surname')
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(validators=[validate_age])
    phone = forms.CharField(max_length=19,
                                   help_text='Enter phone number',
                                   validators=[RegexValidator(
                                       regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
                                       message='Format +375 (29) XXX-XX-XX',
                                   )])
    image = forms.ImageField(required=False)
    city = forms.CharField(max_length=50,
                           help_text='City')
    address = forms.CharField(max_length=200,
                              help_text='Street, Building, etc.')

    class Meta:
        model = ClientUser
        fields = {'username',
                  'first_name', 'last_name', 'email', 'birth_date', 'phone', 'city', 'address',
                  'password1', 'password2', 'image'
                  }

    def save(self, commit: bool = ...) -> Any:
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.birth_date = self.cleaned_data['birth_date']
        user.phone = self.cleaned_data['phone']
        user.city = self.cleaned_data['city']
        user.address = self.cleaned_data['address']
        user.image = self.cleaned_data['image']

        if commit:
            user.save()

        return user
