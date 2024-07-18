from rest_framework import generics
from .models import EducationContent
from .serializers import educationContentserializer

class educationContentListCreate(generics.ListCreateAPIView):
    queryset=EducationContent.objects.all()
    serializer_class=educationContentserializer
    
class educationContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=EducationContent.objects.all()
    serializer_class=educationContentserializer