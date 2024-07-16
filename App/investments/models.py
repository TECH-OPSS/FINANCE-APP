from django.db import models 
from django.contrib.auth import get_user_model 

user=get_user_model()

class investments(models.Model):
    user= models.ForeignKey(user, on_delete=models.CASCADE)
    investment_type=models.CharField(max_lengths=100)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    current_value=models.DecimalField(max_digits=10, decimal_places=2)
    data_invested=models.DataField()
    
    