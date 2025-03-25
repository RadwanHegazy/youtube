from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..serializers import GetPlaylistSerializer, Playlist

class RetrivePlayListByIdAPI (RetrieveAPIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = GetPlaylistSerializer
    lookup_field = 'id'
    queryset = Playlist.objects.all()

class RetrivePlayListByOwnerAPI (ListAPIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = GetPlaylistSerializer
    
    def get_queryset(self):
        return Playlist.objects.filter(
            owner = self.request.user
        )

