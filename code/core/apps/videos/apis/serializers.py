from ..models import Video
from rest_framework import serializers
from apps.users.apis.serializers import UserOwnerSerializer
from ..tasks import parse_resolutions

class CreateVideoSerializer (serializers.ModelSerializer) : 

    class Meta:
        model = Video
        fields = [
            'title',
            'description',
            'thumbnail',
            'original_video',
        ]
        
        
    def save(self, **kwargs):
        request = self.context.get('request')
        data = self.validated_data
        data['owner'] = request.user
        model  = Video.objects.create(**data)
        model.save()
        parse_resolutions.delay(vid_id=model.id)
        return model

    def to_representation(self, instance):
        return {}
    
    
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
