from django.db import models

from users.models.user import CustomerUser


__all__ = [
    'Like',
]

class Like(models.Model):
    user = models.ForeignKey(
        CustomerUser, 
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='likes'
        )
    comment = models.ForeignKey(
       'interactions.Comment',  
        on_delete=models.CASCADE,
        verbose_name='comment',
        related_name='likes'
        )

    class Meta:
        verbose_name_plural  = 'Likes'
        unique_together = ('user', 'comment')
        ordering = ('-created_at',)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} liked comment {self.comment.id}'