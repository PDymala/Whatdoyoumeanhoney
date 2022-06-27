import datetime
from django.db import models
from django.contrib.auth.models import User

class User2(models.Model):
    user_name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    credentials = models.IntegerField(default=2)

    def __str__(self):
        return self.user_name


class Meme(models.Model):
    title = models.CharField('Title', max_length=20)
    prompt = models.CharField('Prompt', max_length=256)
    pantone = models.CharField('Pantone', max_length=20, default="Pantone 0")
    approved = models.BooleanField(default=False)
    add_date = models.DateTimeField('Add date', default=datetime.datetime.now())
    add_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='author')
    likes = models.ManyToManyField(User, related_name='liked', blank=True)

    def __str__(self):
        return self.title
