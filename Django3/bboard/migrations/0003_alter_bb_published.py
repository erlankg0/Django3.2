# Generated by Django 3.2 on 2021-05-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_remove_bb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикаци'),
        ),
    ]
