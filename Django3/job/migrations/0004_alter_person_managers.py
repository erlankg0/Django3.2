# Generated by Django 3.2 on 2021-04-25 14:26

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20210424_0755'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('people', django.db.models.manager.Manager()),
            ],
        ),
    ]