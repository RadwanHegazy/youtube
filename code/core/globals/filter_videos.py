from apps.videos.models import Video


def anonymus_filtering () :
    return Video.objects.filter(is_active=True).order_by('-likes_by','-created_at')

def user_filtering(user) :
    # user_hash_tags = 
    videos = Video.objects.filter(
        is_active=True,
        # write the code of filtering here
    )
    return videos.order_by('-likes_by','-created_at')
    
