from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.playlist.apis.serializers import GetPlaylistSerializer
from apps.playlist.apis.cache import PlaylistCacheQuery


class RetrivePlayListByIdAPI (
    PlaylistCacheQuery,
    RetrieveAPIView
) : 
    permission_classes = [IsAuthenticated]
    serializer_class = GetPlaylistSerializer
    lookup_field = 'id'
    
  

class RetrivePlayListByOwnerAPI (
    PlaylistCacheQuery,
    ListAPIView
) : 
    permission_classes = [IsAuthenticated]
    serializer_class = GetPlaylistSerializer
    

