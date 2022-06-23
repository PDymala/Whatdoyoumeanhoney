from django.db import models


class User(models.Model):
    user_name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')

    def __str__(self):
        return self.user_name


class Meme(models.Model):
    title = models.CharField('Title', max_length=20)
    prompt = models.CharField('Prompt', max_length=256)
    pantone = models.CharField('Pantone', max_length=20)
    approved = models.BooleanField(default=False)
    add_date = models.DateTimeField('Add date')
    add_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
