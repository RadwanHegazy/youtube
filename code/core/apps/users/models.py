from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser) : 
    groups = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    subscriptions = models.ManyToManyField('self', blank=True)
    picture = models.ImageField(upload_to='user-pics/', null=True, blank=True)

    REQUIRED_FIELDS = ['email']
    
    # likes_videos = 
    # history = models
    # hastags = 

    def get_subscriptions(self) : 
        return self.subscriptions.all()
    
    def __str__(self):
        return self.username