from rest_framework import generics
from .models import notification
from .serializers import notificationserializers

class notificationListCreate(generics.ListCreateAPIView):
    queryset=notification.objects.all()
    serializer_class=notificationserializers
    
class notificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=notification.objects.all()
    serializer_class=notificationserializers