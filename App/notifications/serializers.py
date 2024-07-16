from rest_framework import serializers
from .models import notification

class notificationserializers(serializers.ModelSerializer):
    class Meta:
        model=notification
        fields=['id','user','message','created_at','is_read']