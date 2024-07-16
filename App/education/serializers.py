from rest_framework import serializers 
from .models import educationContent

class educationContentserializer(serializers.ModelSerializer):
    class Meta:
        model=educationContent
        fields=['id','title','content_type','created_at']
        