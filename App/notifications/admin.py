from django.contrib import admin
from .models import notification

admin.site.register(notification)
class NotificationAdnmin(admin.ModelAdmin):
    list_display=['user','message','created_at', 'is_read']
    search_fields=['user_username', 'message']
    list_filter=['created_at', 'is_read']