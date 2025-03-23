from django.urls import path
from .views import (
    get,
    create,
    update,
    delete
)

urlpatterns = [
    path('get/<int:video_id>/', get.ListCommentAPI.as_view(), name='get_comments'),
    path('create/<int:video_id>/', create.CreateCommentAPI.as_view(), name='create_comment'),
    path('update/<int:comment_id>/', update.UpdateCommentAPI.as_view(), name='update_comment'),
    path('delete/<int:comment_id>/', delete.DeleteCommentAPI.as_view(), name='delete_comment'),

]