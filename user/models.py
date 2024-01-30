# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    mobileNo=models.CharField(max_length=20, default=0)
    gender=models.CharField(max_length=10, default='Male')
    ageRange=models.CharField(max_length=20,default="20-40")
    
    # Add custom fields here, if needed

    def __str__(self):
        return self.username