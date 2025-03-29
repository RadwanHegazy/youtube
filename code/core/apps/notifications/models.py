from globals.models import TimestampModel, models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notificaion (TimestampModel) : 
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    reciver = models.ForeignKey(User, related_name='reciver', on_delete=models.CASCADE)
    content = models.CharField(max_length=225)

