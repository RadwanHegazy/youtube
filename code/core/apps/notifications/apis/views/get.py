from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from globals.cache import BaseCacheQuery
from ..serializers import (
    NotificaionSerializer,
    Notification
)


class ListNotificationAPI(
    BaseCacheQuery,
    ListAPIView
) : 
    permission_classes = [IsAuthenticated]
    serializer_class = NotificaionSerializer
    cache_key = 'notifications'
    cache_model = Notification

    def get_queryset(self):
        return super().get_queryset().filter(
            reciver = self.request.user
        )