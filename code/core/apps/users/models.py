from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser) : 
    groups = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    subscriptions = models.ManyToManyField('self', blank=True)
    subscribe_to = models.ManyToManyField('self', blank=True)
    picture = models.ImageField(upload_to='user-pics/', null=True, blank=True)

    REQUIRED_FIELDS = ['email']
    
    # liked_videos = models.ManyToManyField('videos.Video', related_name='user_liked_videos' ,blank=True)
    history = models.ManyToManyField('videos.Video', related_name='user_watched_videos' ,blank=True)
    hashtags = models.ManyToManyField('hashtag.Hashtag', related_name='user_hastags_videos' ,blank=True)

    @property
    def get_history(self) : 
        return self.history.all()
    
    def __str__(self):
        return self.username
    
    # def recommended_videos(self) : 
    #     videos_list = []
    #     for hashtag in self.hashtags.all() : 
    #         for video in hashtag.videos.all():
    #             videos_list.append(video.id)

    #     return set(videos_list)
