from rest_framework.generics import DestroyAPIView
from apps.comment.models import Comment
from globals.permissions import IsCommentOwner

class DeleteCommentAPI(DestroyAPIView) : 
    permission_classes = [IsCommentOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'comment_id'

    def get_queryset(self):
        return Comment.objects.filter(owner=self.request.user)