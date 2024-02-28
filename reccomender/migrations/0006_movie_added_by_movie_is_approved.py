# Generated by Django 4.2.5 on 2024-02-28 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import reccomender.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reccomender', '0005_alter_movie_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(default=reccomender.models.get_admin_user_id, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
