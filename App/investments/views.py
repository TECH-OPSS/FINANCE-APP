from rest_framework import generics 
from .models import investments 
from .Serializers import investmentsSerializers

class investmentListCreate(generics.ListCreateAPIView):
    queryset=investments.objects.all()
    serializer_class=investmentsSerializers
    
class investmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = investments.objects.all()
    serializer_class=investmentsSerializers