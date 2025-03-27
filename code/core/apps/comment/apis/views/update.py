from rest_framework.generics import UpdateAPIView
from ..serializers import UpdateCommentSerializer
from apps.comment.models import Comment
from globals.permissions import IsCommentOwner
from globals.cache import BaseCacheQuery

class UpdateCommentAPI(
    BaseCacheQuery,
    UpdateAPIView
) : 
    serializer_class = UpdateCommentSerializer
    permission_classes = [IsCommentOwner]
    lookup_url_kwarg = 'comment_id'
    lookup_field = 'id'
    cache_key = 'comments'
    cache_model = Comment
    
    def get_queryset(self):
        return super().get_queryset().filter(
            owner = self.request.user
        )
    
    def get_serializer_context(self):
        data = super().get_serializer_context()
        comment = self.get_object()
        data['video'] = comment.video
        return data