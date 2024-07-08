from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.urls import reverse
class BaseField(models.Model):
    """title - models.CharField date_create - models.DateTimeField
    Base field from model Tovar and Respose and other 
    """

    title = models.CharField(max_length=100, db_index=True, null=False,verbose_name='Название')
    date_create = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    class Meta:
        abstract = True

# Create your models here.
class Tovar(BaseField):
    """
    1 - title
    2 - date_create
    3 - description
    """


    user = models.ForeignKey(get_user_model(), models.SET_NULL,verbose_name='Пользователь' ,null=True)
    image = models.ImageField(upload_to='tovarIMG', blank=False, null=True)
    description = models.TextField(blank=True, null=True,verbose_name='Описание')
    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('tovar', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        size = (150,150)
        img.thumbnail(size)
        img.save(self.image.path)

    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('-date_create',)
class Response(BaseField):
    """
    1 - text 
    2 - tovar_rel 
    3 - title
    4 - date_create
    """
    text = models.TextField(verbose_name='Содержимое')
    tovar_rel = models.ForeignKey(Tovar, related_name='responses', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        
