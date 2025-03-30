from django.db.models import QuerySet, Q

def anonymus_filtering (queryset) :
    return queryset.filter(is_active=True).order_by('-likes_by','-created_at')

def user_filtering(user, queryset:QuerySet) :
    return queryset.filter(
        is_active=True
    ).filter(
        Q(hashtags__in=user.hashtags.all()) | 
        Q(owner__in=user.subscribe_to.all())
    ).distinct().order_by('-likes_by', '-created_at')

    
