import os.path

from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import ClientUserManager
from django.urls import reverse


# Create your models here.
class ClientUser(AbstractUser):
    """
    custom user
    """
    first_name = models.CharField(max_length=200,
                                  help_text='Name')
    last_name = models.CharField(max_length=200,
                                 help_text='Surname')
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=19,
                             help_text='Phone Number')
    city = models.CharField(max_length=50,
                            help_text='City')
    address = models.CharField(max_length=200,
                               help_text='Street, Building, etc')
    image = models.ImageField(upload_to='user/%Y/%m/%d', default='static/images/mi_safe.png', null=True)

    objects = ClientUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'birth_date', 'phone', 'city', 'address']


class Client(models.Model):
    """
    module for client
    """
    first_name = models.CharField(max_length=200,
                                  help_text='Name')
    last_name = models.CharField(max_length=200,
                                 help_text='Surname')
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=19,
                             help_text='Phone Number')
    city = models.CharField(max_length=50,
                            help_text='City')
    address = models.CharField(max_length=200,
                               help_text='Street, Building, etc')
    image = models.ImageField(upload_to='user/%Y/%m/%d', default='static/images/mi_safe.png', null=True)

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.first_namename, self.last_name, self.city)
