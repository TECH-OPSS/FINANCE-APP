from rest_framework import generics
from .models import educationContent
from .serializers import educationContentserializer

class educationContentListCreate(generics.ListCreateAPIView):
    queryset=educationContent.objects.all()
    serializer_class=educationContentserializer
    
class educationContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=educationContent.objects.all()
    serializer_class=educationContentserializer