from django.db.models.signals import post_save, post_delete
from .models import Video
from django.dispatch import receiver
from django.core.cache import cache
from .documents import VideoDocument
from elasticsearch.helpers.errors import BulkIndexError

@receiver(post_save, sender=Video)
def update_cache(created, instance, **other) : 
    cache.delete('videos')
    VideoDocument().update(instance)
    
@receiver(post_delete, sender=Video)
def update_cache(instance, **other) : 
    cache.delete('videos')
    try :
        VideoDocument().update(instance, action='delete')
    except BulkIndexError:
        pass

