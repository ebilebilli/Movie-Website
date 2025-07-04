from django.db import models

from users.models.user import CustomerUser
from movies.models.movie import Movie

__all__ = [
    'Bookmark'
]


class Bookmark(models.Model):
    user = models.ForeignKey(
        CustomerUser, 
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='bookmarks'
        )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name='Movie',
        related_name='bookmarks'
        )
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural  = 'Bookmarks'
        unique_together = ('user', 'movie')
        ordering = ('-created_at',)
    
    def __str__(self):
        return f'{self.user} added movie: {self.movie.title} to bookmarks'