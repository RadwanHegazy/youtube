from ..models import Video
from rest_framework import serializers
from apps.users.apis.serializers import UserOwnerSerializer
from ..tasks import parse_resolutions
from apps.video_media.serializers import VideoMediaSerializer


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


class ListVideosSerializer(serializers.ModelSerializer) :
    owner = UserOwnerSerializer()
    
    class Meta:
        model = Video
        fields = [
            'id',
            'owner',
            'title',
            'thumbnail',
            'created_at',
            'viewers_counter',
            'duration',
        ]


class GetVideoSerializer(ListVideosSerializer) :
    get_list_video_media = VideoMediaSerializer(many=True)

    class Meta:
        model = Video
        fields = [
            'id',
            'owner',
            'title',
            'thumbnail',
            'created_at',
            'viewers_counter',
            'description',
            'get_likes_by_counter',
            'get_dislikes_by_counter',
            'get_list_video_media',
            'duration',
        ]