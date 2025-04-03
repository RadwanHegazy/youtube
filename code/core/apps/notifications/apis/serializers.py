from ..models import Notification
from rest_framework import serializers
from apps.users.apis.serializers import UserOwnerSerializer

class NotificaionSerializer (serializers.ModelSerializer) : 
    sender = UserOwnerSerializer()

    class Meta:
        model = Notification
        fields = [
            'id',
            'sender',
            'content',
        ]