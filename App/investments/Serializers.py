from rest_framework import serializers
from .models import investments

class investmentsSerializers(serializers.ModelSerializer):
    class Meta:
        model=investments
        fields=['id', 'user', 'investment_type', 'amount_invested', 'current_value' 'date_invested']
