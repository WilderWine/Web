from django.db import models
from django.urls import reverse

# Create your models here.


class FurnitureCategory(models.Model):
    category = models.CharField(max_length=25, help_text='Category of Furniture')

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[str(self.category)])

    def __str__(self):
        return self.category


class FurnitureCollection(models.Model):
    collection = models.CharField(max_length=25, help_text='Collection to that item belongs')

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[str(self.collection)])

    def __str__(self):
        return self.collection


class Furniture(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    code = models.CharField(max_length=8)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(FurnitureCategory, on_delete=models.SET_NULL, null=True)
    collection = models.ForeignKey(FurnitureCollection, on_delete=models.SET_NULL, null=True)
    purchase_count = models.PositiveIntegerField(default=0)
    quantity = models.IntegerField()
    PRODUCTION_STATUS = (
        ('p', 'Produced'),
        ('s', 'Stopped')
    )

    attributes = models.CharField(max_length=2,
                                  choices=PRODUCTION_STATUS,
                                  help_text="state of production")

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


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
        return '{0}, {1}, {2}'.format(self.first_name, self.last_name, self.city)
