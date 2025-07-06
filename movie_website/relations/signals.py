from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from relations.models.category import Category
from relations.models.actor import Actor
from relations.models.director import Director
from relations.models.release_date import ReleaseDate


# Category caches
@receiver(post_save, sender=Category)
@receiver(post_delete, sender=Category)
def clear_cache_for_categories(sender, instance, **kwargs):
    category_id = instance.id
    cache.delete('Categories')
    cache.delete(f'Movies_by_category_{category_id}')


# Actor caches
@receiver(post_save, sender=Actor)
@receiver(post_delete, sender=Actor)
def clear_cache_for_actor(sender, instance, **kwargs):
    actor_id = instance.id
    cache.delete(f'Actor_detail_{actor_id}')
    cache.delete(f'Movies_by_actor_{actor_id}')


# Director caches
@receiver(post_save, sender=Director)
@receiver(post_delete, sender=Director)
def clear_cache_for_director(sender, instance, **kwargs):
    director_id = instance.id
    cache.delete(f'Director_detail_{director_id}')
    cache.delete(f'Movies_by_director_{director_id}')


# Category caches
@receiver(post_save, sender=ReleaseDate)
@receiver(post_delete, sender=ReleaseDate)
def clear_cache_for_release_dates(sender, instance, **kwargs):
    release_date_id = instance.id
    cache.delete('Release_dates')
    cache.delete(f'Movies_by_release_date_{release_date_id}')


