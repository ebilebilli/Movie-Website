from django.db import models

from users.models.user import CustomerUser
from movies.models.movie import Movie


class Watchlist(models.Model):
    user = models.ForeignKey(
        CustomerUser, 
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='watchlists'
        )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name='Movie',
        related_name='watchlists'
        )
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural  = 'Watchlists'
        unique_together = ('user', 'movie')
        ordering = ('-created_at',)
    
    def __str__(self):
        return f'{self.user} added movie: {self.movie.title} to watchlist'