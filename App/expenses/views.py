from rest_framework import generics 
from .models import expenses
from .Serializers import expensesSerializers

class expensesListCreate(generics.ListCreateAPIView):
    queryset = expenses.objects.all()
    serializer_class = expensesSerializers
    
class expensesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = expenses.objects.all()
    Serializers_class = expensesSerializers
