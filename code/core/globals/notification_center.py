from dj_notification.notify import send_notification
from apps.notifications.models import Notification

class NotificationService : 
    
    def __init__(self, from_user, to_user, content, title):
        self.to_user = to_user
        self.from_user = from_user
        self.content = content
        self.title = title

    def send(self) : 

        Notification.objects.create(
            sender = self.from_user,
            reciver = self.to_user,
            content = self.content
        )

        send_notification(
            to_user_id=self.to_user.id,
            content = self.content,
            title = self.title
        )

