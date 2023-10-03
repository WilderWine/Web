from django.db import models

# Create your models here.


class Vacancy(models.Model):
    position = models.CharField(max_length=50, null=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    requirements = models.CharField(max_length=300)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.position
