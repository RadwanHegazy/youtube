from rest_framework.generics import RetrieveAPIView, ListAPIView
from ..serializers import ListVideosSerializer, GetVideoSerializer
from apps.videos.models import Video
from django.core.cache import cache
from datetime import timedelta
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