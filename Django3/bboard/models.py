from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Титул")
    content = models.TextField(verbose_name="Контент")
    price = models.FloatField("Цена", blank=True, null=True)
    published = models.DateField("Дата публикаци", auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to="bboard/Y/M/D")
    rubric = models.ForeignKey("Rubric", on_delete=models.PROTECT, null=True, verbose_name='Рубрика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField("Название рубрики", max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = 'Рубрика'
        ordering = ['name']
# Create your models here.
