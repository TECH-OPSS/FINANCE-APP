from rest_framework import serializers
from django.contrib.auth import get_user_model


user = get_user_model ()

class UserSerializers (serializers.ModelSerializer):
    class Meta:
        model= user
        fields= ['id', 'username','email', 'password']
        extra_kwargs = {'password':{'write_only': True}}
        
    def create  (self, validated_data):
        user= user.objects.create_user(validated_data)  # noqa: F823
        return user
        
    
