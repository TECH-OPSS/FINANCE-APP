from django.urls import path 
from .views import expensesListCreate, expensesDetail

urlpatterns=[
    path('', expensesListCreate.as_view(), name='expenses-list-create'),
    path('<int:pk>/', expensesDetail.as_view(), name='expense-detail'),
]