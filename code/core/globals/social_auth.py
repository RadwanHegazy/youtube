import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth import get_user_model
import threading


def save_image_from_url(user, url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Create a temporary file to store the image
        img_temp = NamedTemporaryFile(delete=True)
        for chunk in response.iter_content(1024):
            img_temp.write(chunk)
        img_temp.flush()

        # Save the image to the user's ImageField
        user.picture.save(f"user_{user.id}_profile.jpg", File(img_temp), save=True)
 



def custom_save_data_for_google (*args, **kwargs) : 
    User = get_user_model()

    user = kwargs['user']
    u, created = User.objects.get_or_create(
        username=user['email'].split('@')[0],
        email=user['email']
    )


    if created:
        t = threading.Thread(
            target=save_image_from_url,
            args=(u, user['picture'])
        )

        t.start()
    u.save()
    return u