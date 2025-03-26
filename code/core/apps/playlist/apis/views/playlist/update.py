from rest_framework.generics import UpdateAPIView
from apps.playlist.apis.serializers import UpdatePlaylistSerializer
from globals.permissions import IsPlayListOwner
from apps.playlist.apis.cache import PlaylistCacheQuery


class UpdatePlaylistAPI (
    PlaylistCacheQuery,
    UpdateAPIView
) :
    serializer_class = UpdatePlaylistSerializer
    permission_classes = [IsPlayListOwner]
    lookup_field = 'id'