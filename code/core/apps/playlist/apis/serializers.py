from rest_framework import serializers
from ..models import Playlist
from apps.videos.apis.serializers import GetVideoSerializer
from apps.users.apis.serializers import UserOwnerSerializer
from apps.videos.models import Video
from django.shortcuts import get_object_or_404

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
    
class UpdatePlaylistSerializer(CreatePlayListSerializer) : ...


class AddVideoSerializer (serializers.Serializer) : 
    video_id = serializers.IntegerField()

    def validate(self, attrs):
        video_id = self.attrs.pop('video_id')
        request = self.context.get('request')
        owner = request.user
        video = get_object_or_404(Video, id=video_id, owner=owner)
        playlist = self.context.get('playlist')
        attrs['video'] = video
        attrs['playlist'] = playlist
        return attrs
    
    def save(self, **kwargs):
        video = self.validated_data['video']
        playlist = self.validated_data['playlist']

        if video not in playlist.videos.all() : 
            playlist.videos.add(video)
            playlist.save()

        return playlist

    def to_representation(self, *args, **kwargs):
        return {}
    
class RemoveVideoSerialzier (AddVideoSerializer) : 

    def save(self, **kwargs):
        video = self.validated_data['video']
        playlist = self.validated_data['playlist']

        if video in playlist.videos.all() : 
            playlist.videos.remove(video)
            playlist.save()

        return playlist