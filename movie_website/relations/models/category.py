from django.db import models


__all__ = [
    'Category',
]

class Category(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Category name'
        )

    def __str__(self):
        return self.title