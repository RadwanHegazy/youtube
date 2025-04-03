from rest_framework.generics import DestroyAPIView
from globals.permissions import IsNotificationOwner
from globals.cache import BaseCacheQuery
from ..serializers import (
    NotificaionSerializer,
    Notification
)


class DeleteNotificationAPI(
    BaseCacheQuery,
    DestroyAPIView
) : 
    permission_classes = [IsNotificationOwner]
    serializer_class = NotificaionSerializer
    lookup_field = 'id'
    cache_key = 'notifications'
    cache_model = Notification
