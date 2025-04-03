from rest_framework.permissions import IsAuthenticated

class BaseIsObjOwner(IsAuthenticated) : 
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner



class IsVideoOwner ( BaseIsObjOwner ) : ...

    
class IsCommentOwner( BaseIsObjOwner ) : ...

class IsPlayListOwner ( BaseIsObjOwner ) : ...

class IsNotificationOwner(BaseIsObjOwner) : 

    def has_object_permission(self, request, view, obj):
        return request.user == obj.reciver