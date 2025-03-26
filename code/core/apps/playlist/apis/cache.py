from django.core.cache import cache
from ..models import Playlist
from datetime import timedelta

class PlaylistCacheQuery :

    def get_queryset(self):
        query = cache.get('playlists', None)

        if not query :
            query = Playlist.objects.all()
            cache.set(
                'playlists',
                query,
                timedelta(hours=2).total_seconds()
            )
        
        return query