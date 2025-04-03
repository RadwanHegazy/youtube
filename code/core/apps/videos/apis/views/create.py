from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from ..serializers import (
    CreateVideoSerializer,
    VideoLikeSerializer,
    VideoDisLikeSerializer
)

class CreateVideoAPI (CreateAPIView) : 
    serializer_class = CreateVideoSerializer
    permission_classes = [IsAuthenticated]


class CreateVideoLikeAPI(CreateAPIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = VideoLikeSerializer
    
class CreateVideoDisLikeAPI(CreateAPIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = VideoDisLikeSerializer
