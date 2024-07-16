from django.db import models 
from django.contrib.auth import get_user_model 

user=get_user_model()

class notification(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)