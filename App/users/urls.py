from django.urls import path 
from .views import userProfileDetail

urlpatterns = [
    path('profile/<int:pk>/', userProfileDetail.as_view(), name='profile-detail'),
]
