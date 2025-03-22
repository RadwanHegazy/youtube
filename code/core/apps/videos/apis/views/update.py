from rest_framework.generics import UpdateAPIView
from globals.permissions import IsVideoOwner
from ...models import Video
from ..serializers import UpdateVideoSerializer
class UpdateVideoAPI (UpdateAPIView) : 
    permission_classes = [IsVideoOwner]
    serializer_class = UpdateVideoSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Video.objects.filter(
            owner = self.request.user,
            is_active=True
        )