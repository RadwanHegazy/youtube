from rest_framework.generics import DestroyAPIView
from globals.permissions import IsVideoOwner
from apps.videos.models import Video
from globals.cache import BaseCacheQuery

class DeleteVideoAPI (
    BaseCacheQuery,
    DestroyAPIView
) : 
    permission_classes = [IsVideoOwner]
    lookup_field = 'id'
    cache_key = 'videos'
    cache_model = Video

    def get_queryset(self):
        return super().get_queryset().filter(
            is_active = True,
            owner = self.request.user
        )