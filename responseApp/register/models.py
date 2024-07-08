from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image



class User(AbstractUser):
    photo = models.ImageField(upload_to='avatar',blank=True,null=True, verbose_name='Фото пользователя')

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        size = (150,150)
        img.thumbnail(size)
        img.save(self.photo.path)