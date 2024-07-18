from rest_framework import generics
from .models import Report
from .serializers import ReportSerializers

class ReportListCreate(generics.ListCreateAPIView):
    queryset= Report.objects.all()
    serializer_class=ReportSerializers
    
    
class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Report.objects.all()
    serializer_class=ReportSerializers