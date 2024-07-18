from rest_framework import serializers
from .models import userProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields=['id', 'user','bio', 'birth_date']
        
      