from rest_framework import generics 
from .models import budgets
from .serializers import budgetsserializers

class budgetListCreate(generics.ListCreateAPIView):
    queryset=budgets.objects.all()
    serializer_class=budgetsserializers
    
class budgetsDetail(generics.RetrieveUpdatesDestroyAPIView):
    queryset=budgets.objects.all()
    serializer_class=budgetsserializers