from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from ..serializers import CreatePlayListSerializer

class CreatePlayListAPI (CreateAPIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = CreatePlayListSerializer
    