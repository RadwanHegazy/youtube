from django.core.cache import cache
from datetime import timedelta

class BaseCacheQuery :
    cache_model = None
    cache_key = None

    def get_queryset(self):
    
        if self.cache_model is None:
            raise Exception("cache_model attr can not be empty")
        
        if self.cache_key is None:
            raise Exception("cache_key attr can not be empty")
        
        query = cache.get(self.cache_key, None)

        if not query :
            query = self.cache_model.objects.all()
            cache.set(
                self.cache_key,
                query,
                timedelta(hours=2).total_seconds()
            )
        
        return query