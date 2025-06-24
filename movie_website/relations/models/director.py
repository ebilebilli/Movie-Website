from django.db import models


__all__ = [
    'Director',
]

class Director(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Director name'
        )
    picture = models.ImageField(
        upload_to='director_pictures/',
        verbose_name='Director picture',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    