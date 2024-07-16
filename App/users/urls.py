from django.urls import path 
from .views import UserProfileDetail

urlpatterns = [
    path('profile/<int:pk>/', UserProfileDetail.as_view(), name='profile-detail'),
]
