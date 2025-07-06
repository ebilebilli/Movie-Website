from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from relations.models.actor import Actor
from relations.models.director import Director

# Actor caches
@receiver(post_save, sender=Actor)
@receiver(post_delete, sender=Actor)
def clear_cache_for_actor(sender, instance, **kwargs):
    actor_id = instance.id
    cache.delete(f'Actor_detail_{actor_id}')
    cache.delete(f'Movies_by_actor_{actor_id}')


# Director caches
@receiver(post_save, sender=Actor)
@receiver(post_delete, sender=Actor)
def clear_cache_for_director(sender, instance, **kwargs):
    director_id = instance.id
    cache.delete(f'Director_detail_{director_id}')
    cache.delete(f'Movies_by_director_{director_id}')


