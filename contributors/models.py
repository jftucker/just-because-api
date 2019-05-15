from django.db import models

from rewards.models import Reward


class Contributor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField()
    reward = models.ForeignKey(Reward, on_delete=models.PROTECT, related_name='reward')

    def __str__(self):
        return self.title