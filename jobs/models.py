from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    workers = models.ManyToManyField(User, related_name='workers')

    def __str__(self):
        return self.title