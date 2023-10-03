from django.db import models
from django.urls import reverse

# Create your models here.

# from factory.models import Furniture, Client

# Create your models here.
'''

class Comment(models.Model):
    rating = models.PositiveSmallIntegerField(default=5)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        retu

'''


class Article(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=250)
    image = models.ImageField(upload_to='article_poster/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return '{0}, dated {1}'.format(self.title, self.created)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
