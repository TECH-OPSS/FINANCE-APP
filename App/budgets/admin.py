from django.contrib import admin
from .models import Budget

admin.site.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display=['user','total_budget','spent_amount','start_date','end_date']
    search_fields=['user_username']
    list_filter=['start_date','end_date']