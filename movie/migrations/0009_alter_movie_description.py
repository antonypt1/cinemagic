# Generated by Django 4.2.13 on 2024-06-30 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=241),
        ),
    ]