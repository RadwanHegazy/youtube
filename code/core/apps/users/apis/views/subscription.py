from rest_framework.generics import CreateAPIView
from ..serializers import SubscribeUserSerializer, UnSubsribeUserSerializer
from rest_framework.permissions import IsAuthenticated

class SubscribeUserAPI (CreateAPIView) : 
    permission_classes = IsAuthenticated
    serializer_class = SubscribeUserSerializer

class UnSubscribeUserAPI (CreateAPIView) : 
    permission_classes = IsAuthenticated
    serializer_class = UnSubsribeUserSerializer


