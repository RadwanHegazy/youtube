from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()


class ProfileSerializer (serializers.ModelSerializer) : 

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'full_name',
            'picture',
        ]

class UserOwnerSerializer(serializers.ModelSerializer) : 

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'picture',
            'full_name'
        ]


class BaseSubscriptionSerializer (serializers.Serializer) : 
    user_id = serializers.IntegerField()

    def validate(self, attrs):
        user_id = attrs['user_id']
        request = attrs['request']
        current_user = request.user
        user_to_subscribe = User.objects.filter(id=user_id).exclude(id=current_user.id)

        if not user_to_subscribe.exists(): 
            raise ValidationError({
                'message' : "Invalid User id"
            }) 
        
        self.current_user = current_user
        self.user_to_subscribe = user_to_subscribe.first()
        return attrs
    
    def to_representation(self, *args, **kwargs):
        return {}
    
class SubscribeUserSerializer(BaseSubscriptionSerializer) : 
    
    def save(self, *args, **kwargs):
        self.current_user.subscribe_to.add(self.user_to_subscribe)
        self.current_user.save()

        self.user_to_subscribe.subscriptions.add(self.current_user)
        self.user_to_subscribe.save()


class UnSubsribeUserSerializer (BaseSubscriptionSerializer) : 

    def save(self, *args, **kwargs):
        self.current_user.subscribe_to.remove(self.user_to_subscribe)
        self.current_user.save()

        self.user_to_subscribe.subscriptions.remove(self.current_user)
        self.user_to_subscribe.save()

        
