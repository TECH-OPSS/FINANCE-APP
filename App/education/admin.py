from django.contrib import admin
from .models import EducationContent

admin.site.register(EducationContent)
class EducationContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_type','created_at']
    search_fields = ['title', 'content_type']
    list_filter=['content_type', 'created_at']