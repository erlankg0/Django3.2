# Generated by Django 3.2 on 2021-05-18 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bb',
            name='image',
        ),
    ]
