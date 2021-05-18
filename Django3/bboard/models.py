from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class Bb(models.Model):
    class Kinds(models.TextChoices):
        BUY = 'b', "Куплю"
        SELL = "s", "Продам"
        EXCHANGE = "c", "Обменяю"
        RENT = 'r', "Аренда"

    title = models.CharField(max_length=50,
                             verbose_name="Титул.")  # ,validators=validators.RegexValidator(regex='^.{4,}$'))
    content = models.TextField(verbose_name="Контент")
    price = models.FloatField("Цена", blank=True, null=True)
    published = models.DateTimeField("Дата публикаци", auto_now_add=True, db_index=True)
    rubric = models.ForeignKey("Rubric", on_delete=models.PROTECT, null=True, verbose_name='Рубрика')
    kind = models.CharField(verbose_name="Тип объявления", max_length=1, choices=Kinds.choices, default=Kinds.SELL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
        unique_together = (
            ("title", "price", "published", "kind"),
            ("title", "price", "rubric", "kind")
        )
        get_latest_by = 'published'


class Rubric(models.Model):
    name = models.CharField("Название рубрики", max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = 'Рубрика'
        ordering = ['name']


class AdvUser(models.Model):
    is_activated = models.BooleanField(verbose_name="Активация пользователя", default=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['is_activated']


class Spare(models.Model):
    name = models.CharField(verbose_name="запаная машина", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Добавить запасные."
        verbose_name = "Добавить запасную."
        ordering = ['name']


class Machine(models.Model):
    name = models.CharField(verbose_name="Машина", max_length=100, blank=True, null=True, help_text="Напишите модель "
                                                                                                    "авто и объем "
                                                                                                    "мотора и "
                                                                                                    "тип топлива")
    spare = models.ManyToManyField(Spare, verbose_name="Выбрать засную машину", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Добавить машины."
        verbose_name = "Добавить машину."
        ordering = ['name']
