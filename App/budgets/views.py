from rest_framework import generics 
from .models import Budget
from .serializers import BudgetSerializer

class BudgetListCreate(generics.ListCreateAPIView):
    queryset=Budget.objects.all()
    serializer_class=BudgetSerializer
    
class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Budget.objects.all()
    serializer_class=BudgetSerializer