from rest_framework.generics import CreateAPIView
from ..serializers import CreateVideoSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from apps.videos.models import Video
from rest_framework.response import Response
from globals.notification_center import NotificationService

class CreateVideoAPI (CreateAPIView) : 
    serializer_class = CreateVideoSerializer
    permission_classes = [IsAuthenticated]


class CreateVideoLikeAPI(CreateAPIView) : 
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        video_id = self.kwargs.get('id',None)
        video = get_object_or_404(Video, id=video_id, is_active=True)
        user = self.request.user

        if user not in video.likes_by.all():
            video.likes_by.add(user)
        else:
            video.likes_by.remove(user)
        
        video.save()
        
        notification = NotificationService(
            from_user=self.request.user,
            to_user=video.owner,
            content=f"{self.request.user.full_name} likes your video '{video.title}' ",
            title="New Like",
        )

        notification.send()

        return Response(status=201)

class CreateVideoDisLikeAPI(CreateAPIView) : 
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        video_id = self.kwargs.get('id',None)
        video = get_object_or_404(Video, id=video_id, is_active=True)
        user = self.request.user

        if user not in video.dislikes_by.all():
            video.dislikes_by.add(user)
        else:
            video.dislikes_by.remove(user)
        
        video.save()
        return Response(status=201)
