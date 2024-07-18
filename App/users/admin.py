from django.contrib import admin
from .models import userProfile 

admin.site.register(userProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','bio','birthrate']
    search_fields=['user_username','bio']

