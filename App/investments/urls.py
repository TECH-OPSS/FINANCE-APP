from django.urls import path 
from .views import investmentListCreate, investmentDetail

urlpatterns =[
    path('', investmentListCreate.as_View(), name='investment-list-create'),
    path('<int:pk>/', investmentDetail.as_view(), name ='investments-detail'),
    
]