from django.urls import path
from apps.social_auth.social_views.Google import google



urlpatterns = [
    path('auth/google/', google.GoogleAuthView.as_view()),
    path('auth/google/url/', google.CreateGoogleAuthLinkView.as_view()),
]