from django.db import models
from django.contrib.auth import get_user_model 

user = get_user_model()

class Expense(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    
