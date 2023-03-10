from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    picture = models.ImageField(verbose_name='Изображение места')
    place = models.ForeignKey(
        'Place',
        verbose_name='локация',
        related_name='images',
        on_delete=models.CASCADE,
        null=True,
    )

    position = models.PositiveIntegerField(
            default=0,
            verbose_name='позиция',
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.id} {self.place.title}'
