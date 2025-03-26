from .models import Playlist
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

@receiver(post_save, sender=Playlist)
def remove_cache(*args, **kwargs) : 
    cache.delete('playlists')

@receiver(post_delete, sender=Playlist)
def remove_cache(*args, **kwargs) : 
    cache.delete('playlists')

