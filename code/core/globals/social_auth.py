
def custom_save_data_for_google (*args, **kwargs) : 
    from django.contrib.auth import get_user_model
    User = get_user_model()
    print(kwargs)
    user = kwargs['user'] # the incomming user from the social platfrom
    # u, _ = User.objects.get_or_create(
    #     username=user['email'].split('@')[0],
    #     email=user['email']
    # )
    # u.save()
    u = User.objects.first()
    return u