from apps.videos.models import Video


def anonymus_filtering () :
    return Video.objects.order_by('-likes_by','-created_at')

def user_filtering(user) :
    videos = Video.objects.filter(
        # write the code of filtering here
    )
    return videos.order_by('-likes_by','-created_at')
    
