from apps.users.models import User
from rest_framework_simplejwt.tokens import AccessToken
from apps.hashtag.models import Video, Hashtag
from apps.comment.models import Comment
from apps.playlist.models import Playlist
from uuid import uuid4


def create_user(username=None,email=None,**kwargs) :
    return User.objects.create(
        username = username if username else str(uuid4()),
        email = email if email else str(uuid4()),
        **kwargs
    )

def create_playlist(owner=None, title="test") : 
    return Playlist.objects.create(
        owner = owner if owner else create_user(),
        title=title
    )

def create_video(owner=None, title='test',description='test', is_active=False, hashtags=[]) :
    vid = Video.objects.create(
        owner = owner if owner else create_user(),
        title=title,
        description=description,
        is_active=is_active
    ) 

    for i in hashtags:
        vid.hashtags.add(i)
    
    vid.save()
    return vid

def create_comment(user=None, video=None) :
    return Comment.objects.create(
        owner=user if user else create_user(),
        video=video if video else create_video()
    ) 
def create_hashtag(name='test'):
    return Hashtag.objects.create(name=name)
    

def create_access_token(user=None) : 
    return AccessToken.for_user(
        user = user if user else create_user()
    )

def create_headers(user=None) : 
    str_headers = create_access_token(user if user else create_user())
    return {
        'Authorization' : f"Bearer {str_headers}"
    }
