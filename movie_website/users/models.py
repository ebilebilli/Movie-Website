from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(models.Model):
    email = models.EmailField(
        unique=True,
        verbose_name='Email'  
        )
    username = models.CharField(
        unique=True,
        max_length=20,
        verbose_name='Username'
        )
    birthday = models.DateField(
        verbose_name='Birthday'
        )
    bio = models.TextField(
        max_length=250,
        verbose_name='Bio',
        null=True,
        blank=True
        )
    profile_images = models.ImageField(
        upload_to='profile_images',
        verbose_name='Profile image',
        null=True,
        blank=True
        )
    
    def __str__(self):
        return f'{self.username} - {self.email}'
     