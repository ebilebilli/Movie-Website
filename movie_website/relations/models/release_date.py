from django.db import models
from utils.validators import year_validator


__all__ = [
    'ReleaseDate',
]

class ReleaseDate(models.Model):
    year = models.CharField(
        max_length=4,
        validators=[year_validator],
        verbose_name='Year'
        )
  
    class Meta:
        verbose_name_plural = 'Release dates'
    
    def __str__(self):
        return self.year
    