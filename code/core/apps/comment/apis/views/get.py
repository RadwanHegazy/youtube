from rest_framework.generics import ListAPIView
from ..serializers import ListCommentSerializer
from apps.comment.models import Comment, Video
from django.shortcuts import get_object_or_404

class ListCommentAPI(ListAPIView) : 
    serializer_class = ListCommentSerializer

    def get_queryset(self):
        video_id = self.kwargs.get('video_id', None)
        video = get_object_or_404(Video, id=video_id)
        return Comment.objects.filter(video=video)