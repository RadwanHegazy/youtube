from django.urls import path
from .views import (
    delete,
    get,
    update,
    create
)


urlpatterns = [
    path('v1/upload/', create.CreateVideoAPI.as_view(), name='upload_video'),
    path('v1/get/', get.ListVideoAPI.as_view(), name='list_video'),
    path('v1/user/history/', get.UserHistoryVideoAPI.as_view(), name='user_history'),
    path('v1/user/likes/', get.UserLikedVideosAPI.as_view(), name='user_likes'),
    path('v1/get/<int:id>/', get.RetriveVideoAPI.as_view(), name='retrive_video'),
    path('v1/delete/<int:id>/', delete.DeleteVideoAPI.as_view(), name='delete_video'),
    path('v1/update/<int:id>/', update.UpdateVideoAPI.as_view(), name='update_video'),
    path('v1/like/', create.CreateVideoLikeAPI.as_view(), name='like_video'),
    path('v1/dislike/', create.CreateVideoDisLikeAPI.as_view(), name='dislike_video'),
]