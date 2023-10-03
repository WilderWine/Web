from django.db import models

# Create your models here.


class Faq(models.Model):
    question = models.CharField(max_length=200, null=False)
    answer = models.CharField(max_length=1000, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Faq'
        verbose_name_plural = 'FaqS'

    def __str__(self):
        return self.question
