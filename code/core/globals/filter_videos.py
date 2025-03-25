
def anonymus_filtering (queryset) :
    return queryset.filter(is_active=True).order_by('-likes_by','-created_at')

def user_filtering(user, queryset) :
    videos = queryset.filter(
        is_active=True,
        hashtags__in=user.hashtags.all()
    )
    return videos.order_by('-likes_by','-created_at')

    
