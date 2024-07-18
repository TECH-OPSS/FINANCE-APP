from django.urls import path 
from .views import BudgetListCreate, BudgetDetail


urlpatterns=[
    path('', BudgetListCreate.as_view(), name='budget-list-create'),
    path('<int:pk>/', BudgetDetail.as_view(), name='budget-detail'),
]