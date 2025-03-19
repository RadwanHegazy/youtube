from django.db import models
from apps.videos.models import Video

class VideoMedia (models.Model) : 
    video = models.ForeignKey(Video, related_name='video_media', on_delete=models.CASCADE)
    quality = models.CharField(max_length=10)
    path = models.FilePathField(null=True, blank=True)

    