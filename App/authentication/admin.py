from django.contrib import admin 
from django.contrib.auth import get_user_model

user = get_user_model()

admin.site.register(user)

class userAdmin(admin.ModelAdmin):
    list_display=['username', 'email', 'is_admin', 'is_active']
    search_fields=['username', 'email']
