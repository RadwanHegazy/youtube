from rest_framework.generics import UpdateAPIView
from globals.permissions import IsVideoOwner
from ...models import Video

class UpdateVideoAPI (UpdateAPIView) : 
    permission_classes = [IsVideoOwner]
    lookup_field = 'id'

    def get_queryset(self):
        return Video.objects.filter(
            owner = self.request.user
        )