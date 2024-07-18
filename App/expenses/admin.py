from django.contrib import admin
from .models import Expense

admin.site.register(Expense)

class ExpenseAdmin(admin.ModelAdmin):
    list_display=['user', 'amount', 'category','description','date']
    search_fields=['user_username','category', 'description']
    list_filter=['date','category']
