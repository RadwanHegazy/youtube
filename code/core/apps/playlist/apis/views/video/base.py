from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.playlist.models import Playlist
from django.shortcuts import get_object_or_404

class BasePlaylistVideoAPI (CreateAPIView) : 
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        data = super().get_serializer_context()
        playlist_id = self.kwargs.get('playlist_id')
        playlist = get_object_or_404(Playlist, id=playlist_id, owner=self.request.user)
        data['playlist'] = playlist
        return data