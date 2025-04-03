from .models import Notification
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=Notification)
def update_cache(created, instance, **kwargs) : 
    cache.delete('notifications')

@receiver(post_delete, sender=Notification)
def update_cache(instance, **kwargs) : 
    cache.delete('notifications')
