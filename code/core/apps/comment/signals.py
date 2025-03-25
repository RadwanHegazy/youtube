from django.db.models.signals import post_save, post_delete
from .models import Comment
from django.dispatch import receiver
from django.core.cache import cache

@receiver(post_save, sender=Comment)
def update_cache(created, instance, **other) : 
    cache.delete('comments')

@receiver(post_delete, sender=Comment)
def update_cache(instance, **other) : 
    cache.delete('comments')
