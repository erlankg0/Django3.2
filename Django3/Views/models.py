from django.db import models


class Publisher(models.Model):
    name = models.CharField("Название Издателя", max_length=30)
    address = models.CharField("Адрес Издателя", max_length=100)
    city = models.CharField("Город Издателя", max_length=60)
    state_province = models.CharField("Провинция Издателя", max_length=60)
    country = models.CharField("Страна Издателя", max_length=60)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издателя"
        verbose_name_plural = "Издатели"
        ordering = ['name']


class Author(models.Model):
    salutation = models.CharField("Приведствие", max_length=30)
    name = models.CharField("ФИО Автора", max_length=200)
    email = models.EmailField("Е-Почта")
    headshot = models.ImageField(upload_to="author_image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['name']


class Book(models.Model):
    title = models.CharField("Название книги", max_length=200)
    authors = models.ManyToManyField(Author, verbose_name="Авторы книги")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"
        ordering = ["publication_date"]

# Create your models here.
