# Generated by Django 4.1.3 on 2022-12-19 10:03

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('description_short', models.CharField(max_length=250, verbose_name='Короткое описание')),
                ('description_long', tinymce.models.HTMLField(verbose_name='Описание')),
                ('lng', models.FloatField(verbose_name='Долгота')),
                ('lat', models.FloatField(verbose_name='Широта')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='', verbose_name='Изображение места')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='позиция')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='poster.place', verbose_name='локация')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
