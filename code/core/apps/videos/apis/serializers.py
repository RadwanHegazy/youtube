from ..models import Video
from rest_framework import serializers
from apps.users.apis.serializers import UserOwnerSerializer
from ..tasks import parse_resolutions
from apps.video_media.serializers import VideoMediaSerializer
from django.shortcuts import get_object_or_404
from globals.notification_center import NotificationService
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from ..documents import VideoDocument, fields

class VideoDocumentSerializer(DocumentSerializer):
    
    class Meta:
        document = VideoDocument
        fields = (
            'id',
            'owner',
            'title',
            'thumbnail',
            'created_at',
            'viewers_counter',
            'duration',
            'description',
        )

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


class BaseVideoLikeSerializer(serializers.Serializer) : 
    video_id = serializers.IntegerField()

    def validate(self, attrs):
        video_id = attrs.get('video_id')
        video = get_object_or_404(Video, id=video_id, is_active=True)
        request = self.context.get('request')

        attrs['video'] = video
        attrs['user'] = request.user
        return attrs
    
    def to_representation(self, *args, **kwargs):
        return {}
    

class VideoLikeSerializer(BaseVideoLikeSerializer) : 

    def save(self, **kwargs):
        user = self.validated_data['user']
        video = self.validated_data['video']

        if user not in video.likes_by.all():
            video.likes_by.add(user)
        else:
            video.likes_by.remove(user)
        
        video.save()
        
        notification = NotificationService(
            from_user=user,
            to_user=video.owner,
            content=f"{user.full_name} likes your video '{video.title}' ",
            title="New Like",
        )

        notification.send()

class VideoDisLikeSerializer(BaseVideoLikeSerializer) : 

    def save(self, **kwargs):
        user = self.validated_data['user']
        video = self.validated_data['video']

        if user not in video.dislikes_by.all():
            video.dislikes_by.add(user)
        else:
            video.dislikes_by.remove(user)
        
        video.save()

