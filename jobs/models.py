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
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    points = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    isFinished = models.BooleanField(default=False)
    location = models.CharField(max_length=50, null=True, blank=True)
    liked = models.ManyToManyField(User, related_name='liked')
    saved = models.ManyToManyField(User, related_name='saved')
    joined = models.ManyToManyField(User, related_name='joined')
    contributors = models.ManyToManyField(Contributor, related_name='contributors')
    rewards = models.ManyToManyField(Reward, related_name='rewards')
    workers = models.ManyToManyField(User, related_name='workers')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')

    def __str__(self):
        return self.title