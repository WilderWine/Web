from django.db import models

# Create your models here.


class Promo(models.Model):
    promocode = models.CharField(max_length=15, null=False)
    slogan = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    is_active = models.BooleanField(null=False, default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Promo'
        verbose_name_plural = 'Promos'

    def __str__(self):
        return self.promocode
