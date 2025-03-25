from rest_framework.generics import CreateAPIView
from ..serializers import CreateCommentSerializer
from apps.comment.models import Comment, Video
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class CreateCommentAPI(CreateAPIView) : 
    serializer_class = CreateCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        data = super().get_serializer_context()
        video_id = self.kwargs.get('video_id', None)
        video = get_object_or_404(Video, id=video_id)
        data['video'] = video
        return data