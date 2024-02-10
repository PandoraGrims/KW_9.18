from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

STATUS_CHOICES = [
    ('moderation', 'На модерации'),
    ('published', 'Опубликовано'),
    ('rejected', 'Отклонено'),
    ('deleted', 'На удаление'),
]


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Advertisement(models.Model):
    photo = models.ImageField(upload_to='photos', verbose_name='Фотография ', blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,
                               default=1, related_name="advertisements", verbose_name="Автор", null=False,
                               blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=475, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='moderation')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "advertisements"
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT,
                               default=1, related_name="comments", verbose_name="Автор", null=False, blank=False)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(verbose_name="Текст", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
