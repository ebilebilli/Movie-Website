from django.db import models


__all__ = [
    'Actor',
]

class Actor(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Actor name'
        )
    picture = models.ImageField(
        upload_to='actor_pictures/',
        verbose_name='Actor picture',
        null=True,
        blank=True
    )
    
    