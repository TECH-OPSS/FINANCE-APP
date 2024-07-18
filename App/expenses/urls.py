from django.urls import path 
from .views import ExpenseListCreate, ExpenseDetail

urlpatterns=[
    path('', ExpenseListCreate.as_view(), name='expense-list-create'),
    path('<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
]