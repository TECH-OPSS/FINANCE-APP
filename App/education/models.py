from django.db import models 

class EducationContent(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    content_type=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    