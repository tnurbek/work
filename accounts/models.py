from django.db import models
from django.contrib.auth.models import User
from .validators import validate_size


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', validators=[validate_size])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}_{self.id}'


class Log(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    file = models.CharField(max_length=255, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.file}'

    class Meta:
        verbose_name_plural = 'Image Change Logs'