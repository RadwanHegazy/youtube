from rest_framework.generics import RetrieveAPIView, ListAPIView
from ..serializers import ListVideosSerializer, GetVideoSerializer
from apps.videos.models import Video
from django.core.cache import cache
from datetime import timedelta
from globals.filter_videos import (
    anonymus_filtering,
    user_filtering
)

class ListVideoAPI (ListAPIView) :
    serializer_class = ListVideosSerializer

    def get_queryset(self):
        user = self.request.user
        query = cache.get('videos', None)

        if not query :
            query = Video.objects.all()
            cache.set('videos', query, timedelta(hours=2).total_seconds())
            
        if user.is_anonymous:
            query = anonymus_filtering(query)
        else:
            query = user_filtering(user, query)
        
        return query

class RetriveVideoAPI(RetrieveAPIView) : 
    serializer_class = GetVideoSerializer
    queryset = Video.objects.filter(is_active=True)
    lookup_field = 'id'

    def get_queryset(self):
        query = cache.get('videos', None)

        if not query : 
            query = Video.objects.all()
            cache.set('videos', query, timedelta(hours=2).total_seconds())

        return query.filter(is_active=True)