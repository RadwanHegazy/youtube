from rest_framework.generics import CreateAPIView
from ..serializers import CreateVideoSerializer
from rest_framework.permissions import IsAuthenticated

class CreateVideoAPI (CreateAPIView) : 
    serializer_class = CreateVideoSerializer
    permission_classes = [IsAuthenticated]
    