from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.playlist.apis.serializers import GetPlaylistSerializer
from globals.cache import BaseCacheQuery
from apps.playlist.models import Playlist


class RetrivePlayListByIdAPI (
    BaseCacheQuery,
    RetrieveAPIView
) : 
    serializer_class = GetPlaylistSerializer
    lookup_field = 'id'
    cache_key = 'playlists'
    cache_model = Playlist
    
  

class RetrivePlayListByOwnerAPI (
    BaseCacheQuery,
    ListAPIView
) : 
    permission_classes = [IsAuthenticated]
    serializer_class = GetPlaylistSerializer
    cache_key = 'playlists'
    cache_model = Playlist

    def get_queryset(self):
        return super().get_queryset().filter(
            owner = self.request.user
        )
