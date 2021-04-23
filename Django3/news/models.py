from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название новости")
    content = models.TextField(null=True, blank=True, verbose_name="Контент новости")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменения")
    photo = models.ImageField(upload_to="photos/%Y/%M/%D", verbose_name="Загрузка картинки")
    is_published = models.BooleanField(verbose_name="Публикация", help_text="Выбор публикации")

    def __str__(self):
        return self.title
# Create your models here.
