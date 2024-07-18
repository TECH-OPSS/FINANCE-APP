from django.urls import path 
from .views import ReportListCreate, ReportDetail


urlpatterns= [
    path('', ReportListCreate.as_view(), name='report-list-create'),
    path('<int:pk>/',ReportDetail.as_view(), name='report-detail'),
]