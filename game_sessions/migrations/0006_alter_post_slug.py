# Generated by Django 4.2.11 on 2024-05-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_sessions', '0005_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.SlugField(max_length=200, unique=True), verbose_name=models.SlugField(max_length=200, unique=True)),
        ),
    ]
