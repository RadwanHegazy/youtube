from django.urls import path
from apps.social_auth.social_views.Google import google
from .views import (
    profile, 
    subscription
)


urlpatterns = [
    path('v1/auth/google/', google.GoogleAuthView.as_view(), name='google_auth'),
    path('v1/auth/google/url/', google.CreateGoogleAuthLinkView.as_view(), name='google_url'),

    path('v1/profile/', profile.ProfileViewAPI.as_view(), name='profile'),
    path('v1/subscribe/', subscription.SubscribeUserAPI.as_view(), name='subscribe_user'),
    path('v1/unsubscribe/', subscription.UnSubscribeUserAPI.as_view(), name='unsubscribe_user'),
]