from django.db import models
from django.core.exceptions import ValidationError

from users.models.user import CustomerUser
from movies.models.movie import Movie
from .like import Like


__all__ = [
    'Comment',
]

class Comment(models.Model):
    user = models.ForeignKey(
        CustomerUser, 
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='comments'
        )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name='Movie',
        related_name='comments'
        )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Parent',
        related_name='replies'
        )

    text = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural  = 'Comments'

    @property
    def like_count(self):
        return Like.objects.filter(comment=self).count()
    
    def clean(self):
        if self.parent and self.parent.movie != self.movie:
            raise ValidationError('Reply comment must be for the same movie as the parent comment')

    def __str__(self):
        return self.text
        
 
    