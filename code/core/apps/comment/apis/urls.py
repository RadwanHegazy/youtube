from django.urls import path
from .views import (
    get,
    create,
    update,
    delete
)

urlpatterns = [
    path('v1/get/<int:video_id>/', get.ListCommentAPI.as_view(), name='get_comments'),
    path('v1/create/<int:video_id>/', create.CreateCommentAPI.as_view(), name='create_comment'),
    path('v1/update/<int:comment_id>/', update.UpdateCommentAPI.as_view(), name='update_comment'),
    path('v1/delete/<int:comment_id>/', delete.DeleteCommentAPI.as_view(), name='delete_comment'),

]