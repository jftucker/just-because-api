from django.db import models
from django.contrib.auth import get_user_model

from rewards.models import Reward
from contributors.models import Contributor

User = get_user_model()


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    size = models.IntegerField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    liked = models.ManyToManyField(User, related_name='liked')
    saved = models.ManyToManyField(User, related_name='saved')
    joined = models.ManyToManyField(User, related_name='joined')
    isFinished = models.BooleanField(default=False)
    contributors = models.ManyToManyField(Contributor, related_name='contributors')
    rewards = models.ManyToManyField(Reward, related_name='rewards')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    workers = models.ManyToManyField(User, related_name='workers')

    def __str__(self):
        return self.title