from rest_framework.generics import DestroyAPIView
from apps.comment.models import Comment
from globals.permissions import IsCommentOwner
from globals.cache import BaseCacheQuery

class DeleteCommentAPI(
    BaseCacheQuery,
    DestroyAPIView
) : 
    permission_classes = [IsCommentOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'comment_id'
    cache_key = 'comments'
    cache_model = Comment

    def get_queryset(self):
        return super().get_queryset().filter(
            owner = self.request.user
        )