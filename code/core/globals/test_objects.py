from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from uuid import uuid4

User = get_user_model()

def create_user(username=None,email=None,**kwargs) :
    return User.objects.create(
        username = username if username else str(uuid4()),
        email = email if email else str(uuid4()),
        **kwargs
    )


def create_access_token(user=None) : 
    return AccessToken.for_user(
        user = user if user else create_user()
    )

def create_headers(user=None) : 
    str_headers = create_access_token(user if user else create_user())
    return {
        'Authorization' : f"Bearer {str_headers}"
    }
