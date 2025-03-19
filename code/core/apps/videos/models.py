from django.db import models
from django.contrib.auth import get_user_model
from globals.models import TimestampModel

User = get_user_model()


class Video (TimestampModel) : 
    owner = models.ForeignKey(User, related_name='video_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    description = models.TextField()
    likes_by = models.ManyToManyField(User,  related_name='likes_by_users',blank=True)
    dislikes_by = models.ManyToManyField(User, related_name='dislikes_by_users' ,blank=True)
    thumbnail = models.ImageField(upload_to='video-thumbnails/')
    viewers = models.ManyToManyField(User, related_name='video_viwers', blank=True)
    viewers_counter = models.IntegerField(default=0)
    duration = models.CharField(max_length=20, null=True, blank=True)
    original_video = models.FileField(upload_to='video-original/')
    is_active = models.BooleanField(default=False)
    
    @property
    def get_unique_viewers_counter(self) : 
        return self.viewers.count()

    @property
    def get_likes_by_counter(self) : 
        return self.likes_by.count()
    
    @property
    def get_dislikes_by_counter(self) : 
        return self.dislikes_by.count()
    
