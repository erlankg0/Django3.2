from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(verbose_name="Имя", max_length=50)
    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    size = models.CharField("Выбро размера одежды", max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = "Имена"
        ordering = ['name']
        db_table = 'Person'


class Musician(models.Model):
    author = models.ForeignKey(Person, verbose_name='Выберите человека', on_delete=models.CASCADE)
    instrument = models.CharField(verbose_name="Инструмент", max_length=70)

    def __str__(self):
        return self.instrument

    class Meta:
        verbose_name = "Музыкант"
        verbose_name_plural = "Музыканты"
        ordering = ['instrument']


class Album(models.Model):
    artist = models.ManyToManyField(Musician)
    name = models.CharField(verbose_name="Название альбома", max_length=100)
    release_date = models.DateField()
    nus_star = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['name']
# Create your models here.
