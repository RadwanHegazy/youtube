from rest_framework.generics import ListAPIView
from ..serializers import ListCommentSerializer
from apps.comment.models import Comment, Video
from django.shortcuts import get_object_or_404
from globals.cache import BaseCacheQuery

class ListCommentAPI(
    BaseCacheQuery,
    ListAPIView
) : 
    serializer_class = ListCommentSerializer
    cache_key = 'comments'
    cache_model = Comment

    def get_queryset(self):
        video_id = self.kwargs.get('video_id', None)
        video = get_object_or_404(Video, id=video_id)
        return super().get_queryset().filter(video=video)