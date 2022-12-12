from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.title   
    
