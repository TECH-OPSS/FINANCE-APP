from django.contrib import admin
from .models import Report 

admin.site.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display=['user','report_type','generated_at']
    search_fields=['user_username','report_type']
    list_filter=['generated_at', 'report_type']
