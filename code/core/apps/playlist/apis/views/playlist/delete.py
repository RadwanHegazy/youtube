from rest_framework.generics import DestroyAPIView
from globals.permissions import IsPlayListOwner
from globals.cache import BaseCacheQuery
from apps.playlist.models import Playlist

class DeletePlaylistAPI (
    BaseCacheQuery,
    DestroyAPIView
) :
    permission_classes = [IsPlayListOwner]
    lookup_field = 'id'
    cache_key = 'playlists'
    cache_model = Playlist

