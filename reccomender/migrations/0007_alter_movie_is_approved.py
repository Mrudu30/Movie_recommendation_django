# Generated by Django 4.2.5 on 2024-02-28 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reccomender', '0006_movie_added_by_movie_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
