from rest_framework import serializers
from .models import budgets


class budgetsserializers(serializers.Modelserializers):
    class Meta:
        model = budgets
        fields = ['id', 'user','total_budget', 'spent_amount','start_date','end_date']
    