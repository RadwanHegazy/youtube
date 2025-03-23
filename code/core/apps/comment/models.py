from globals.models import TimestampModel, models
from django.contrib.auth import get_user_model
from apps.videos.models import Video

User = get_user_model()


class Comment (TimestampModel) : 
    owner = models.ForeignKey(User, related_name='comment_owner', on_delete=models.CASCADE)
    content = models.TextField()
    video = models.ForeignKey(Video, related_name='for_video', on_delete=models.CASCADE)

    def __str__(self):
        return self.content