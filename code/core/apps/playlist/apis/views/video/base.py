from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.playlist.models import Playlist
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from rest_framework.exceptions import PermissionDenied

class BasePlaylistVideoAPI (CreateAPIView) : 
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        data = super().get_serializer_context()
        playlist_id = self.kwargs.get('playlist_id')
        playlist = get_object_or_404(Playlist, id=playlist_id)
        if playlist.owner != self.request.user : 
            raise PermissionDenied("Permission Denied")
        data['playlist'] = playlist
        return data