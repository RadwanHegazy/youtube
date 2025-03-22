from rest_framework.generics import RetrieveAPIView, ListAPIView
from ..serializers import ListVideosSerializer, GetVideoSerializer
from apps.videos.models import Video
from globals.filter_videos import (
    anonymus_filtering,
    user_filtering
)

class ListVideoAPI (ListAPIView) :
    serializer_class = ListVideosSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            query = anonymus_filtering()
        else:
            query = user_filtering(user)
        
        return query

class RetriveVideoAPI(RetrieveAPIView) : 
    serializer_class = GetVideoSerializer
    queryset = Video.objects.filter(is_active=True)
    lookup_field = 'id'