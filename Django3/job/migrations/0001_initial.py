# Generated by Django 3.2 on 2021-04-20 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1, verbose_name='Выбро размера одежды')),
            ],
            options={
                'verbose_name': 'Имя',
                'verbose_name_plural': 'Имена',
                'db_table': 'Person',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(max_length=70, verbose_name='Инструмент')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.person', verbose_name='Выберите человека')),
            ],
            options={
                'verbose_name': 'Музыкант',
                'verbose_name_plural': 'Музыканты',
                'ordering': ['instrument'],
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название альбома')),
                ('release_date', models.DateField()),
                ('nus_star', models.PositiveSmallIntegerField(default=1)),
                ('artist', models.ManyToManyField(to='job.Musician')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['name'],
            },
        ),
    ]
