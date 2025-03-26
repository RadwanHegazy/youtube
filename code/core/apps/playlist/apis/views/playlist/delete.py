from rest_framework.generics import DestroyAPIView
from globals.permissions import IsPlayListOwner
from apps.playlist.apis.cache import PlaylistCacheQuery

class DeletePlaylistAPI (
    PlaylistCacheQuery,
    DestroyAPIView
) :
    permission_classes = [IsPlayListOwner]
    lookup_field = 'id'

