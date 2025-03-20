from apps.videos.models import Video


def anonymus_filtering () :
    return Video.objects.filter(is_active=True).order_by('-likes_by','-created_at')

def user_filtering(user) :
    videos = Video.objects.filter(
        is_active=True,
        hashtags__in=user.hashtags.all()
    )
    return videos.order_by('-likes_by','-created_at')

    
