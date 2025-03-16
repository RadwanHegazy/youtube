from rest_framework.generics import RetrieveAPIView
from ..serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

class ProfileViewAPI (RetrieveAPIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    
    def get_object(self):
        return self.request.user
    