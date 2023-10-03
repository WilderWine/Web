from django.db import models
from login.models import ClientUser

# Create your models here.


class Comment(models.Model):
    rating = models.PositiveSmallIntegerField(default=5)
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return 'Comment by {0}, {1}'.format(self.client, self.created)
