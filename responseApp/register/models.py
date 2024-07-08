from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    photo = models.ImageField(upload_to='avatar',blank=True,null=True, verbose_name='Фото пользователя')
