from django.urls import path 
from .views import educationContentListCreate, educationContentDetail


urlpatterns=[
    path('',educationContentListCreate.as_view(), name='educationcontent-list-create'),
    path('<int:pk>/', educationContentDetail.as_view(), name='educationcontent-detail'),
]