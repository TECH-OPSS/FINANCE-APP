from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class userProfile(models.Model):
    user=models.OneToOneField(user,on_delete=models.CASCADE)
    bio=models.TextField (blank=True)
    birth_date = models.DateField(null=True, blank=True)


