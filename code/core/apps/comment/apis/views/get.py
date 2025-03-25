from rest_framework.generics import ListAPIView
from ..serializers import ListCommentSerializer
from apps.comment.models import Comment, Video
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from datetime import timedelta

class ListCommentAPI(ListAPIView) : 
    serializer_class = ListCommentSerializer

    def get_queryset(self):
        video_id = self.kwargs.get('video_id', None)
        video = get_object_or_404(Video, id=video_id)

        query = cache.get('comments', None)

        if not query : 
            query = Comment.objects.all()
            cache.set('comments', query, timedelta(hours=2).total_seconds())

        return query.filter(video=video)