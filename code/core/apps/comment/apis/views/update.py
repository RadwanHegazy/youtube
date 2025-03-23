from rest_framework.generics import UpdateAPIView
from ..serializers import UpdateCommentSerializer
from apps.comment.models import Comment, Video
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class UpdateCommentAPI(UpdateAPIView) : 
    serializer_class = UpdateCommentSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     video_id = self.kwargs.get('id', None)
    #     video = get_object_or_404(Video, id=video_id)
    #     return Comment.objects.filter(video=video)
    
    def get_serializer_context(self):
        data = super().get_serializer_context()
        video_id = self.kwargs.get('comment_id', None)
        video = get_object_or_404(Video, id=video_id)
        data['video'] = video
        return data