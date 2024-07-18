from rest_framework import generics
from .models import userProfile 
from .Serializers import UserProfileSerializer


class userProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = UserProfileSerializer
    


