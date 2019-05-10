from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title