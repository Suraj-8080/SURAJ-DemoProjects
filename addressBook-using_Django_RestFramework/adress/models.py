from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_name = models.EmailField(max_length=100)
    phone_name = models.CharField(max_length=100)
    
class Address(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    address= models.TextField()


