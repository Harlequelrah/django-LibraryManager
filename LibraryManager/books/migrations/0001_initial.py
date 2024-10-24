# Generated by Django 5.1.2 on 2024-10-23 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='titre')),
                ('label', models.CharField(max_length=100, verbose_name='description')),
                ('author', models.CharField(max_length=150, verbose_name='auteur')),
                ('publication_date', models.DateTimeField(verbose_name='année de publication')),
                ('cover_image', models.ImageField(upload_to='', verbose_name='couverture')),
                ('available', models.BooleanField(default=True, verbose_name='disponibilité')),
                ('stars', models.IntegerField(default=0)),
                ('genre', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='genres', to='books.genre')),
            ],
        ),
    ]
