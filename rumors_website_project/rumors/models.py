from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Community(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        default='the_default.jpg', upload_to='community_pics')

    def __str__(self):
        return f'{self.title} Profile'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    date_posted = models.DateTimeField(default=timezone.now)
    Community = models.ForeignKey(Community, on_delete=models.CASCADE)
