from django.db import models


class Reward(models.Model):
    item = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField()

    def __str__(self):
        return self.title