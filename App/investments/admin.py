from django.contrib import admin
from .models import investments

admin.site.register(investments)
class invenstmentsAdmin(admin.ModelAdmin):
    list_display=['user','investment_type','amount_invested','current_value','date_invested']
    search_fields=['user_username','investment_type']
    list_filter=['date_investment','investment_type']
