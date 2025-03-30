from rest_framework.generics import RetrieveAPIView, ListAPIView
from ..serializers import ListVideosSerializer, GetVideoSerializer
from apps.videos.models import Video
from rest_framework.permissions import IsAuthenticated
from globals.cache import BaseCacheQuery
from globals.filter_videos import (
    anonymus_filtering,
    user_filtering
)

class ListVideoAPI (
    BaseCacheQuery,
    ListAPIView
) :
    serializer_class = ListVideosSerializer
    cache_key = 'videos'
    cache_model = Video

    def get_queryset(self):
        user = self.request.user
        query = super().get_queryset()

        if user.is_anonymous:
            query = anonymus_filtering(query)
        else:
            query = user_filtering(user, query)
        
        return query

class RetriveVideoAPI(
    BaseCacheQuery,
    RetrieveAPIView
) : 
    serializer_class = GetVideoSerializer
    cache_model = Video
    cache_key = 'videos'
    lookup_field = 'id'

    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=True
        )
    
    def get_object(self):
        vid = super().get_object()
        user = self.request.user
        if user.is_authenticated:
            user.history.add(vid)
            user.save()
        return vid
    

class UserHistoryVideoAPI (
    ListAPIView
) :
    serializer_class = ListVideosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.get_history
    
class UserLikedVideosAPI (
    BaseCacheQuery,
    ListAPIView
) :
    serializer_class = ListVideosSerializer
    permission_classes = [IsAuthenticated]
    cache_key = 'videos'
    cache_model = Video
    
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(
            likes_by__in=[self.request.user]
        )
