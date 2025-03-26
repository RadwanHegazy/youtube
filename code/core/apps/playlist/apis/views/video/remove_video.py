from apps.playlist.apis.serializers  import RemoveVideoSerialzier
from .base import BasePlaylistVideoAPI

class RemovePlaylistVideoAPI (BasePlaylistVideoAPI) : 
    serializer_class = RemoveVideoSerialzier
