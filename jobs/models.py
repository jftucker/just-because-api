from django.db import models
from users.models import CustomUser


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='author')
    workers = models.ManyToManyField(CustomUser, related_name='workers')

    def __str__(self):
        return self.title