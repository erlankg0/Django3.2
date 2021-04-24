from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name="Имя автора", max_length=100)
    age = models.PositiveSmallIntegerField('Возвраст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'
        ordering = ['name']


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'
        ordering = ['name']


class Book(models.Model):
    name = models.CharField("Название книги", max_length=300)
    pages = models.IntegerField("Страницы книги")
    price = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Цена')
    rating = models.FloatField(verbose_name='Рейтинг')
    authors = models.ManyToManyField(Author, verbose_name='Автор/Авторы')
    publisher = models.ForeignKey(Publisher, verbose_name='Издатель', on_delete=models.CASCADE)
    pubdate = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'


class Store(models.Model):
    name = models.CharField(max_length=300, verbose_name='Магазин')
    books = models.ManyToManyField(Book, verbose_name='Выборки книги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['name']
# Create your models here.
