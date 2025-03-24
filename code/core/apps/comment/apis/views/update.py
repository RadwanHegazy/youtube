from rest_framework.generics import UpdateAPIView
from ..serializers import UpdateCommentSerializer
from apps.comment.models import Comment, Video
from django.shortcuts import get_object_or_404
from globals.permissions import IsCommentOwner


class UpdateCommentAPI(UpdateAPIView) : 
    serializer_class = UpdateCommentSerializer
    permission_classes = [IsCommentOwner]
    lookup_url_kwarg = 'comment_id'
    lookup_field = 'id'
    
    def get_queryset(self):
        return Comment.objects.filter(owner=self.request.user)

    def get_serializer_context(self):
        data = super().get_serializer_context()
        comment = self.get_object()
        data['video'] = comment.video
        return data