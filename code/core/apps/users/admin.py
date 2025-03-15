from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

@admin.register(User)
class UserPanel(admin.ModelAdmin) : 
    list_display = ['username','email','full_name']


admin.site.unregister(Group)