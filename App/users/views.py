from rest_framework import generics
from .models import UserProfile 
from .Serializers import UserProfileSerializer


class userProfileDetail(generics.RetriveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    


