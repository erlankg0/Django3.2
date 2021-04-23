from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=200, verbose_name="Порода собаки")
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name

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


class Blog(models.Model):
    name = models.CharField(verbose_name="Категория блога", max_length=75)
    tag_line = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория блога"
        verbose_name_plural = "Категории блогов"
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(verbose_name="Имя Автора", max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['name']


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=250, verbose_name="подзаголовок", null=True, blank=True)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now=True)
    mod_date = models.DateField(auto_now_add=True)
    authors = models.ManyToManyField(Author, verbose_name="Авторы")
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['-headline']


class Group(models.Model):
    name = models.CharField(verbose_name='Имя группы.', max_length=150)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_join = models.DateTimeField(auto_now=True)
    invite_reason = models.CharField(max_length=70)

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Членство'
        verbose_name_plural = 'Члены группы'
        ordering = ['group']


# -----------------------------------------------------------------------------------


