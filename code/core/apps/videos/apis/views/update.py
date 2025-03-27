from rest_framework.generics import UpdateAPIView
from globals.permissions import IsVideoOwner
from apps.videos.models import Video
from apps.videos.apis.serializers import UpdateVideoSerializer
from globals.cache import BaseCacheQuery

class UpdateVideoAPI (
    BaseCacheQuery,
    UpdateAPIView
) : 
    permission_classes = [IsVideoOwner]
    serializer_class = UpdateVideoSerializer
    lookup_field = 'id'
    cache_key = 'videos'
    cache_model = Video

    def get_queryset(self):
        return super().get_queryset().filter(
            is_active = True,
            owner = self.request.user
        )
    
 