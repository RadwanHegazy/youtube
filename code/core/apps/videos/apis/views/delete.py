from rest_framework.generics import DestroyAPIView
from globals.permissions import IsVideoOwner
from ...models import Video

class DeleteVideoAPI (DestroyAPIView) : 
    permission_classes = [IsVideoOwner]
    lookup_field = 'id'

    def get_queryset(self):
        return Video.objects.filter(
            owner = self.request.user
        )