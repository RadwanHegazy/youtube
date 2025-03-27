from rest_framework.generics import UpdateAPIView
from apps.playlist.apis.serializers import UpdatePlaylistSerializer
from globals.permissions import IsPlayListOwner
from globals.cache import BaseCacheQuery
from apps.playlist.models import Playlist

class UpdatePlaylistAPI (
    BaseCacheQuery,
    UpdateAPIView
) :
    serializer_class = UpdatePlaylistSerializer
    permission_classes = [IsPlayListOwner]
    lookup_field = 'id'
    cache_key = 'playlists'
    cache_model = Playlist