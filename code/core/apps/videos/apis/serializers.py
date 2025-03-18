from ..models import Video
from rest_framework import serializers
from apps.users.apis.serializers import UserOwnerSerializer

class CreateVideoSerializer (serializers.ModelSerializer) : 
    # video = serializers.FileField()

    class Meta:
        model = Video
        fields = [
            'owner',
            'title',
            'description',
            'thumbnail',
        ]

    def validate(self, attrs):
        request = self.context.get('request')
        attrs['owner'] = request.user
        return attrs
    
class UpdateVideoSerializer (CreateVideoSerializer) : ...


class GetVideoSerializer(serializers.ModelSerializer) :
    owner = UserOwnerSerializer()

    class Meta:
        model = Video
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'thumbnail',
            'viewers_counter',
            'get_likes_by_counter',
            'get_dislikes_by_counter',
        ]
