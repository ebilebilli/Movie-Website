from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

from relations.models.category import Category
from relations.models.director import Director
from relations.models.actor import Actor
from utils.validators import release_date_validator


__all__ =[
    'Movie',
]

class Movie(models.Model):
    categories = models.ManyToManyField(
        Category,
        verbose_name='Categories',
        related_name='movies'
        )
    director = models.ForeignKey(
        Director,
        on_delete=models.PROTECT,
        verbose_name='Director',
        related_name='movies',
        null=True,
        blank=True
        )
    actors = models.ManyToManyField(
        Actor,
        verbose_name='Actors',
        related_name='movies',
        )

    title = models.CharField(
        max_length=30,
        verbose_name='Movie name'
        )
    description = models.TextField(
        max_length=255,
        verbose_name='Description'
        )
    release_date = models.DateField(
        verbose_name='Release date',
        validators=[release_date_validator]
        )
    duration = models.PositiveIntegerField(
        verbose_name='Duration in minutes'
        )
    rating = models.FloatField(
        verbose_name='Rating',
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )
    poster = models.ImageField(
        upload_to='posters/',
        verbose_name='Poster' 
        )
    video = models.FileField(
        upload_to='videos/',
        verbose_name='Video',
        )
    trailer_url = models.URLField(
        verbose_name='Trailer url',
        null=True, 
        blank=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )
    slug = models.SlugField(
        unique=True, 
        blank=True
        )
    
    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ('-created_at')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
