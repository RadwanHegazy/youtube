from django.urls import path
from .views import (
    get,
    delete
)

urlpatterns = [
    path('v1/get/', get.ListNotificationAPI.as_view(), name='get_notifications'),
    path('v1/delete/<int:id>/', delete.DeleteNotificationAPI.as_view(), name='delete_notifications'),
]