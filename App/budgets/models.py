from django.db import models 
from django.contrib.auth import get_user_model

user = get_user_model()

class Budget(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    total_budget=models.DecimalsField(max_digits=10, decimal_places=2)
    spent_amount=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date=models.DateField()
    end_date=models.DateField()

