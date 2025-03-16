from django.urls import path
from apps.social_auth.social_views.Google import google
from .views import profile


urlpatterns = [
    path('auth/google/', google.GoogleAuthView.as_view(), name='google_auth'),
    path('auth/google/url/', google.CreateGoogleAuthLinkView.as_view(), name='google_url'),

    path('profile/', profile.ProfileViewAPI.as_view(), name='profile')
]