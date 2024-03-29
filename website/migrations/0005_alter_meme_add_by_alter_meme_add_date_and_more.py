# Generated by Django 4.0.4 on 2022-06-26 11:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0004_user2_alter_meme_add_by_alter_meme_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='add_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meme',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 26, 13, 18, 7, 583303), verbose_name='Add date'),
        ),
        migrations.AlterField(
            model_name='meme',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
