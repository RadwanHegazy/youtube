from django.urls import path
from .views.playlist import (
    get,
    create,
    update,
    delete
)

from .views.video import (
    add_video,
    remove_video
)

urlpatterns = [
    path('v1/update/<int:id>/', update.UpdatePlaylistAPI.as_view(), name='update_playlist'),
    path('v1/delete/<int:id>/', delete.DeletePlaylistAPI.as_view(), name='delete_playlist'),
    path('v1/get/<int:id>/', get.RetrivePlayListByIdAPI.as_view(), name='retrive_playlist_id'),
    path('v1/get/owner/', get.RetrivePlayListByOwnerAPI.as_view(), name='retrive_playlist_owner'),
    path('v1/create/', create.CreatePlayListAPI.as_view(), name='create_playlist'),
    path('v1/add/video/<int:playlist_id>/',add_video.AddPlaylistVideoAPI.as_view(), name='add_playlist_video'),
    path('v1/remove/video/<int:playlist_id>/',remove_video.RemovePlaylistVideoAPI.as_view(), name='remove_playlist_video'),
]