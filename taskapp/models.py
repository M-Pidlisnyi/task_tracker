from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    
