from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from movies.models.movie import Movie

@receiver(post_save, sender=Movie)
@receiver(post_delete, sender=Movie)
def clear_cache(sender, **kwargs):
    cache.delete_pattern('search_*') 