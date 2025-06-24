from django.db import models


class CustomeUser(models.Model):
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
        verbose_name='Bio'
    )
     