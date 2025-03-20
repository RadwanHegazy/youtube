from django.urls import path
from .views import (
    delete,
    get,
    update,
    create
)


urlpatterns = [
    path('upload/', create.CreateVideoAPI.as_view(), name='upload_video'),
    path('get/', get.ListVideoAPI.as_view(), name='list_video'),
    path('get/<int:id>/', get.RetriveVideoAPI.as_view(), name='retrive_video'),
    path('delete/<int:id>/', delete.DeleteVideoAPI.as_view(), name='delete_video'),
    path('update/<int:id>/', update.UpdateVideoAPI.as_view(), name='update_video'),
]