from django.db.models.signals import post_save, post_delete
from .models import Video
from django.dispatch import receiver
from django.core.cache import cache
from .documents import VideoDocument

@receiver(post_save, sender=Video)
def update_cache(created, instance, **other) : 
    cache.delete('videos')

@receiver(post_delete, sender=Video)
def update_cache(instance, **other) : 
    cache.delete('videos')

@receiver(post_save, sender=Video)
def update_video_document(sender, instance, **kwargs):
    VideoDocument().update(instance)

@receiver(post_delete, sender=Video)
def delete_video_document(sender, instance, **kwargs):
    VideoDocument().update(instance, action='delete')