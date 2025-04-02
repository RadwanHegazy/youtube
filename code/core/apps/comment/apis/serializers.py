from ..models import Comment
from rest_framework import serializers
from apps.users.apis.serializers import UserOwnerSerializer
from globals.notification_center import NotificationService

class ListCommentSerializer(serializers.ModelSerializer) : 
    owner = UserOwnerSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'owner'
        ]

class BaseCommentSerializer(serializers.ModelSerializer) : 
    
    class Meta:
        model = Comment
        fields = [
            'content'
        ]

    def validate(self, attrs):
        request = self.context.get('request')
        video = self.context.get('video')
        user = request.user
        attrs['owner'] = user
        attrs['video'] = video
        return attrs

class CreateCommentSerializer(BaseCommentSerializer) : 
    
    def save(self, **kwargs):
        super().save(**kwargs)
        user = self.validated_data.get('user')
        video = self.validated_data.get('video')
        notificaion = NotificationService(
            from_user=user,
            to_user=video.owner,
            content=f"{user.full_name} comment in your video '{video.title}'.",
            title="New Comment",
        )

        notificaion.send()


class UpdateCommentSerializer (BaseCommentSerializer) : ... 