from rest_framework import serializers
from .models import Report 

class ReportSerializers(serializers.ModelSerializer):
    class Meta: 
        model=Report 
        fields=['id','user','report_type','data','generated_at'] 
    
