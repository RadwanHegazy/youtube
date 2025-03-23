from ..models import Comment
from rest_framework import serializers
from apps.users.apis.serializers import UserOwnerSerializer

class ListCommentSerializer(serializers.ModelSerializer) : 
    owner = UserOwnerSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'owner'
        ]

class CreateCommentSerializer(serializers.ModelSerializer) : 
    
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

class UpdateCommentSerializer (CreateCommentSerializer) : ... 