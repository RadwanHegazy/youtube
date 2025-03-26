from apps.playlist.apis.serializers  import AddVideoSerializer
from .base import BasePlaylistVideoAPI

class AddPlaylistVideoAPI (BasePlaylistVideoAPI) : 
    serializer_class = AddVideoSerializer
