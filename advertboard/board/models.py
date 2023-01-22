from django.db import models
# импорт поля для хранения всякого разного содержимого
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


CATEGORY = {
    ('Танки', 'Танки'),
    ('Хилы', 'Хилы'),
    ('ДД', 'ДД'),
    ('Торговцы', 'Торговцы'),
    ('Гилдмастеры', 'Гилдмастеры'),
    ('Квестгиверы', 'Квестгиверы'),
    ('Кузнецы', 'Кузнецы'),
    ('Кожевники', 'Кожевники'),
    ('Зельевары', 'Зельевары'),
    ('Мастера заклинаний', 'Мастера заклинаний')
}


class Advertisment(models.Model):
    head = models.CharField(max_length=255)
    content_upload = RichTextUploadingField(blank=True,null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=255, choices=CATEGORY, default='Танки')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.head

    def get_absolute_url(self):
        return reverse('adsdetail', args=[str(self.id)])


class Responses(models.Model):
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    acceptresponse = models.BooleanField(
        default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advertisment, on_delete=models.CASCADE)
