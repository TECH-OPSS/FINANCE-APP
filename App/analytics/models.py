from django.db import models
from django.contrib.auth import get_user_model


user=get_user_model()


class Report(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    report_type=models.CharField(max_length=100)
    data=models.JSONField()
    generated_at =models.DateTimeField(auto_now_add=True)
    
    
    