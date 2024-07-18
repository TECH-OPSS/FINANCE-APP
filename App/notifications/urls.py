from django.urls import path 
from .views import notificationListCreate, notificationDetail

urlpatterns=[
    path('', notificationListCreate.as_view(), name='notification-list-create'),
    path('<int:pk>', notificationDetail.as_view(), name='notification-detail'),
]