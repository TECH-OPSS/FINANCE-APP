from django.urls import path 
from .views import notificationsListCreate, notificationsDetail

urlpatterns=[
    path('', notificationsListCreate.as_view(), name='notification-list-create'),
    path('<int:pk>', notificationsDetail.as_view(), name='notification-detail'),
]