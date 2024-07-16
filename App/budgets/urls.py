from django.urls import path 
from .views import budgetsListCreate, budgetsDetail


urlspatterns=[
    path('', budgetsListCreate.as_view(), name='budget-list-create'),
    path('<int:pk>/', budgetsDetail.as_view(), name='budget-detail'),
]