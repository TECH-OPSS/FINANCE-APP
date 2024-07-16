from rest_framework import Serializers
from .models import expenses 

class ExpenseSerializer(Serializers.ModelSerializer):
    class Meta:
        model= expenses
        fields = ['id','user','amount','description','date']