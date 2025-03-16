from globals.models import TimestampModel, models
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment (TimestampModel) : 
    owner = models.ForeignKey(User, related_name='comment_owner', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content