from django.urls import path
from .views import (
    get,
    create
)

urlpatterns = [
    path('get/v1/<int:id>/', get.RetrivePlayListByIdAPI.as_view(), name='retrive_playlist_id'),
    path('get/v1/owner/', get.RetrivePlayListByOwnerAPI.as_view(), name='retrive_playlist_owner'),
    path('get/v1/create/', create.CreatePlayListAPI.as_view(), name='create_playlist'),
]