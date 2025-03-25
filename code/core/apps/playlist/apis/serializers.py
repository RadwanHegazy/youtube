from rest_framework import serializers
from ..models import Playlist
from apps.videos.apis.serializers import GetVideoSerializer
from apps.users.apis.serializers import UserOwnerSerializer

    
class GetPlaylistSerializer(serializers.ModelSerializer) : 
    owner = UserOwnerSerializer()
    get_video_list = GetVideoSerializer(many=True)

    class Meta:
        model = Playlist
        fields = [
            'id',
            'owner',
            'title',
            'get_total_videos',
            'get_videos_list',
        ]

class CreatePlayListSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Playlist
        fields = [
            'id',
            'title'
        ]

    def validate(self, attrs):
        request = self.context.get('request')
        attrs['owner'] = request.user
        return attrs