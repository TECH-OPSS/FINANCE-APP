from rest_framework import serializers 
from .models import EducationContent

class educationContentserializer(serializers.ModelSerializer):
    class Meta:
        model=EducationContent
        fields=['id','title','content_type','created_at']
        