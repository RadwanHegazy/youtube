from django.db.models.signals import post_save, post_delete
from .models import Video
from django.dispatch import receiver
from django.core.cache import cache

@receiver(post_save, sender=Video)
def update_cache(created, instance, **other) : 
    cache.delete('videos')

@receiver(post_delete, sender=Video)
def update_cache(instance, **other) : 
    cache.delete('videos')
