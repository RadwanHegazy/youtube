from rest_framework.generics import DestroyAPIView
from apps.comment.models import Comment
from globals.permissions import IsCommentOwner

class DeleteCommentAPI(DestroyAPIView) : 
    queryset = Comment.objects.all()
    permission_classes = [IsCommentOwner]
    lookup_field = 'comment_id'