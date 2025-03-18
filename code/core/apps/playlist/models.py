from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Playlist(models.Model) : 
    owner = models.ForeignKey(User, related_name='playlist_owner', on_delete=models.CASCADE)
    videos = models.ManyToManyField('videos.Video')
    title = models.CharField(max_length=100)

    @property
    def get_total_videos(self) -> int: 
        return self.videos.count()
    
    def __str__(self):
        return self.title