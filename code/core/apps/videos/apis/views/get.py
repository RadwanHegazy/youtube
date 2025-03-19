from rest_framework.generics import RetrieveAPIView, ListAPIView
from ..serializers import GetVideoSerializer, Video
from globals.filter_videos import (
    anonymus_filtering,
    user_filtering
)

class ListVideoAPI (ListAPIView) :
    serializer_class = GetVideoSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            query = anonymus_filtering()
        else:
            query = user_filtering(user)
        
        return query

class RetriveVideoAPI(RetrieveAPIView) : 
    serializer_class = GetVideoSerializer
    queryset = Video.objects.filter(is_active=True)
    lookup_field = 'id'